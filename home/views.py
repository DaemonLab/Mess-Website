import io
from datetime import date, timedelta

import pandas as pd
from allauth.socialaccount.models import SocialAccount
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.files import File
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_date
from django.utils.timezone import now
from home.models import (About, Allocation, AllocationForm, Cafeteria,
                         Carousel, Caterer, CatererBills, Contact, Form,
                         LeftShortRebate, LongRebate, Period, PeriodAutumn22,
                         PeriodSpring23, Rebate, RebateAutumn22,
                         RebateSpring23, Rule, Semester, ShortRebate, Student,
                         StudentBills, UnregisteredStudent, Update)

from .utils.get_rebate_bills import get_rebate_bills
from .utils.rebate_checker import is_not_duplicate, max_days_rebate

# Create your views here.


def home(request):
    """
    Display the Home Page :model:`home.models.home`.

    **Template:**

    :template:`home/home.html`

    """
    aboutInfo = About.objects.all()
    update = Update.objects.filter().order_by("time_stamp")
    caterer = Caterer.objects.filter(visible=True).all()
    carousel = Carousel.objects.all()
    context = {
        "about": aboutInfo,
        "updates": update,
        "caterer": caterer,
        "carousel": carousel,
        'all_caterer' : caterer
    }
    return render(request, "home.html", context)


def rules(request):
    """
    Display the Rules Page :model:`home.models.rules`.

    **Template:**

    :template:`home/rules.html`

    """
    rules = Rule.objects.all()
    shortRebates = ShortRebate.objects.all()
    params = {
        "rule": rules,
        "shortRebate": shortRebates,
    }

    return render(request, "rules.html", params)


def caterer(request, name):
    """
    Display the Caterer Page :model:`home.models.caterer`.

    **Template:**

    :template:`home/caterer.html`

    """
    caterer = Caterer.objects.get(name=name,visible=True)
    context = {"caterer": caterer}
    return render(request, "caterer.html", context)


def links(request):
    """
    Display the Forms Page :model:`home.models.links`.

    **Template:**

    :template:`home/links.html`

    """
    form = Form.objects.all()
    context = {"form": form}
    return render(request, "links.html", context)


def cafeteria(request):
    """
    Display the Cafeteria Page :model:`home.models.cafeteria`.

    **Template:**

    :template:`home/cafeteria.html`

    """
    cafeteria = Cafeteria.objects.all()
    context = {"cafeteria": cafeteria}
    return render(request, "cafeteria.html", context)


def contact(request):
    """
    Display the Contact Page :model:`home.models.contacts`.

    **Template:**

    :template:`home/contact.html`

    """
    contact = Contact.objects.all()
    context = {"contact": contact}
    return render(request, "contact.html", context)


@login_required
def rebate(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    Gets the data from the rebate form checks for the validity of the rebate filled,
    adds the rebte to the rebate model and rebate bills of that semester.
    This form can only be accessed by the Institute community

    **Template:**

    :template:`rebateForm.html`
    """
    text = ""
    list = []
    try:
        print(request.user.email)
        allocation_id = Allocation.objects.filter(email__email=str(request.user.email))
        try:
            for period in Period.objects.all():
                if period.end_date>date.today()+timedelta(1):
                    period_obj=period
                    break
            print(period_obj)
            allocation_id = Allocation.objects.get(
                email__email=str(request.user.email),
                period = period_obj
            )
            key = str(allocation_id.student_id) 
        except:
            key="You are not allocated for current period, please contact the dining warden to allocate you to a caterer"
    except Allocation.DoesNotExist:
        key = "Signed in account does not does not have any allocation ID"     
    if request.method == "POST" and request.user.is_authenticated:
        try:
            start_date = parse_date(request.POST["start_date"])
            end_date = parse_date(request.POST["end_date"])
            rebate_days = ((end_date - start_date).days) + 1
            before_rebate_days = (start_date - date.today()).days
            try:
                student = Student.objects.filter(
                    email=str(request.user.email)
                ).first()
                period = allocation_id.period.Sno
                period_start = allocation_id.period.start_date
                period_end = allocation_id.period.end_date
                if(rebate_days>7):
                    text="Max no of days for rebate is 7"
                elif not period_start<=start_date:
                    text = "Please fill the rebate of this period only"    
                elif not is_not_duplicate(student, start_date, end_date):
                    text = "You have already applied for rebate for these dates"
                else:
                    if not period_start<=start_date<=period_end:
                        short_left_rebate = LeftShortRebate(
                            email=str(request.user.email),
                            start_date=start_date,
                            end_date=end_date,
                            date_applied=date.today(),
                        )
                        short_left_rebate.save()
                        text = "You have successfully submitted the rebate, it will get addedd to your bills in the next period."
                        upper_cap_check=-1
                    elif not period_start<=end_date<=period_end:
                        short_left_rebate = LeftShortRebate(
                            email=str(request.user.email),
                            start_date=period_end+timedelta(days=1),
                            end_date=end_date,
                            date_applied=date.today(),
                        )
                        short_left_rebate.save()
                        end_date=period_end
                        upper_cap_check = max_days_rebate(student, start_date, period_end, period_obj)
                    else:
                        upper_cap_check = max_days_rebate(student, start_date, end_date, period_obj)
                    if upper_cap_check >= 0:
                        text = (
                            "You can only apply for max 8 days in a period. Days left for this period: "
                            + str(upper_cap_check)
                        )
                    elif text=="" and (rebate_days) <= 7 and rebate_days >= 2 and before_rebate_days >= 2:
                        r = Rebate(
                            email=student,
                            allocation_id=allocation_id,
                            start_date=start_date,
                            end_date=end_date,
                            approved=False,
                        )
                        r.save()
                        text = "You have successfully submitted the rebate, subject to approval of Office of Dining Warden. Thank You!"
                    elif 0 < rebate_days < 2:
                        text = "Min no of days for rebate is 2"
                    elif before_rebate_days < 2:
                        text = "Form needs to be filled atleast 2 days prior the comencement of leave."
                    elif rebate_days > 7:
                        text = "Max no of days for rebate is 7"
                    elif before_rebate_days < 0:
                        text = "Please enter the correct dates"
                    elif text=="":
                        text = "Your rebate application has been rejected due to non-compliance of the short term rebate rules"
            except Allocation.DoesNotExist:
                text = "Email ID does not match with the allocation ID"
        except Exception as e:
            print(e)
            text = "Ohh No! an unknown ERROR occured, Please inform about it immediatly to the Dining Wadern."
    context = {"text": text, "key": key, "list": list}
    return render(request, "rebateForm.html", context)

@staff_member_required(redirect_field_name="/", login_url="/")
def allocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/allocation.html`

    Gets the data from the allocation csv,
    parses each row and allocates each student an allocation ID and caterer for that month.
    Which can be then exported in the admin page.
    CSV should be imported from /allocation/ url only
    This form can only be accessed by the Institute's admin
    """
    messages = ""
    if (
        request.method == "POST"
        and request.user.is_authenticated
        and request.user.is_staff
    ):
        try:
            file = request.FILES["csv"]
            file_extension = file.name.split('.')[-1].lower()
            if file_extension == 'csv':
                csv_data = pd.read_csv(io.StringIO(file.read().decode('utf-8')))
            elif file_extension == 'xlsx':
                csv_data = pd.read_excel(file, engine='openpyxl')
            print(csv_data.head())

            for record in csv_data.to_dict(orient="records"):
                try:
                    if 'First Preference' in csv_data.columns:
                        first_pref = str(record["First Preference"]).capitalize()
                        caterer1 = Caterer.objects.get(name=first_pref)
                    else:
                        first_pref =None
                    if 'Second Preference' in csv_data.columns:
                        second_pref = str(record["Second Preference"]).capitalize()
                        caterer2 = Caterer.objects.get(name=second_pref)
                    else:
                        second_pref=None
                    if 'Third Preference' in csv_data.columns:
                        third_pref = str(record["Third Preference"]).capitalize()
                        caterer3 = Caterer.objects.get(name=third_pref)
                    else:
                        third_pref=None

                    #  getting period object
                    if 'Period' in csv_data.columns and 'Semester' in csv_data.columns:
                        period = str(record["Period"]).capitalize()
                        semester = str(record["Semester"]).capitalize()
                        period_obj = Period.objects.get(Sno=period, semester=Semester.objects.get(name=semester))
                    else:
                        period_obj = Period.objects.filter().last()

                    # getting high tea
                    high_tea = record["High Tea"]
                    print(high_tea)
                    if(high_tea=="Yes" or high_tea==True or high_tea=="TRUE"):
                        high_tea=True
                    else:
                        high_tea=False
                    
                    student = Student.objects.filter(email=record["Email"]).first()
                    if(student==None):
                        messages+=str(record["Email"])
                    print(student)

                    if caterer1.student_limit>=0:
                        caterer1.student_limit-=1
                        caterer1.save(update_fields=["student_limit"])
                        caterer=caterer1
                    elif caterer2 and caterer2.student_limit>=0:
                        caterer2.student_limit-=1
                        caterer2.save(update_fields=["student_limit"])
                        caterer=caterer2
                    elif caterer3 and caterer3.student_limit>=0:
                        caterer3.student_limit-=1
                        caterer3.save(update_fields=["student_limit"])
                        caterer=caterer3
                    student_id = str(caterer.name[0])
                    if high_tea == True:
                        student_id += "H"
                    else:
                        student_id+="NH"
                    student_id += str(caterer.student_limit)
                    allocation = Allocation(
                        email=student,
                        student_id=student_id,
                        period=period_obj,
                        caterer=caterer,
                        high_tea=high_tea,
                        first_pref=first_pref,
                        second_pref=second_pref,
                        third_pref=third_pref,
                    )
                    allocation.save()
                    student_bill = StudentBills.objects.get_or_create(email=student, semester=period_obj.semester)
                    UnregisteredStudent.objects.filter(email=student.email).delete()
                except Exception as e:
                    print(e)
            messages += "Form submitted. Please check the admin page."
        except Exception as e:
            print(e)
            messages = "Invalid CSV file"
    period_obj = Period.objects.filter().last()
    caterer_list = []
    for caterer in Caterer.objects.filter(visible=True).all():
        caterer_high_tea = Allocation.objects.filter(caterer=caterer, high_tea=True,period=period_obj).count()
        caterer_total = Allocation.objects.filter(caterer=caterer,period=period_obj).count()
        caterer_left = caterer.student_limit
        caterer_list.append([caterer.name,caterer_high_tea,caterer_total,caterer_left])
    context = {"messages": messages,"list": caterer_list}
    return render(request, "admin/allocation.html", context)

@login_required
def addLongRebateBill(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/longRebate.html`

    Gets the data from the log term rebate form , and adds it to the coresponding rebate bill
    This form can only be accessed by the Institute's admin
    """
    text = ""
    if request.method == "POST" and request.user.is_authenticated:
        try:
            start_date = parse_date(request.POST["start_date"])
            end_date = parse_date(request.POST["end_date"])
            days = (end_date - start_date).days + 1
            student = Student.objects.get(email=request.user.email)
            if not is_not_duplicate(student, start_date, end_date):
                text = "You have already applied for rebate for these dates"
            else:
                try:
                    file=request.FILES["img"]
                    print(file)
                    long = LongRebate(
                        email=student,
                        start_date=start_date,
                        end_date=end_date,
                        days=days,
                        approved=False,
                        file=file,
                    )
                    long.save()
                    text = "Long Term rebate added Successfully"
                except Exception as e:
                    text = "Allocation ID for the entered email does not exist"
                    print(e)
        except:
            text = "Email ID does not exist in the database. Please eneter the correct email ID"
    context = {"text": text}
    return render(request, "longRebate.html", context)

@login_required
def allocationForm(request):
    """
    Display the Allocation Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/allocationForm.html`

    Gets the data from the allocation form , and adds it to the coresponding allocation model
    """
    caterer_list = Caterer.objects.filter(visible=True).all()
    alloc_form = AllocationForm.objects.filter(active=True).last()
    try:
        student = Student.objects.filter(email=str(request.user.email)).last()
        key=student.email
        text = ""
        if alloc_form.start_time and alloc_form.start_time>now() and alloc_form.end_time and alloc_form.end_time<now():
            text = "Form is closed for now."
        if Allocation.objects.filter(email=student,period=alloc_form.period).exists():
            allocation_id = Allocation.objects.filter(email=student,period=alloc_form.period).last()
            text = "You have already filled the form for this period. with first preference:" + allocation_id.first_pref + " second preference:" + allocation_id.second_pref
        if request.method == "POST" and request.user.is_authenticated :
            try:
                period_obj = alloc_form.period
                high_tea = request.POST["high_tea"]
                if caterer_list.count()<1:
                    first_pref = None
                else:
                    first_pref = request.POST["first_pref"]
                    caterer1 = Caterer.objects.get(name=first_pref)
                if caterer_list.count()<2:
                    second_pref = None
                else:
                    second_pref = request.POST["second_pref"]
                    caterer2 = Caterer.objects.get(name=second_pref)
                if caterer_list.count()<3:
                    third_pref = None
                else:
                    third_pref = request.POST["third_pref"]
                    caterer3 = Caterer.objects.get(name=third_pref)

                if caterer1.student_limit>=0:
                    caterer1.student_limit-=1
                    caterer1.save(update_fields=["student_limit"])
                    caterer=caterer1
                elif caterer2 and caterer2.student_limit>=0:
                    caterer2.student_limit-=1
                    caterer2.save(update_fields=["student_limit"])
                    caterer=caterer2
                elif caterer3 and caterer3.student_limit>=0:
                    caterer3.student_limit-=1
                    caterer3.save(update_fields=["student_limit"])
                    caterer=caterer3
                student_id = str(caterer.name[0])
                if high_tea == True:
                    student_id += "H"
                else:
                    student_id+="NH"
                student_id += str(caterer.student_limit)
                allocation = Allocation(
                    email=student,
                    student_id=student_id,
                    period=period_obj,
                    caterer=caterer,
                    high_tea=high_tea,
                    first_pref=first_pref,
                    second_pref=second_pref,
                    third_pref=third_pref,
                )
                allocation.save()
                student_bill = StudentBills.objects.get_or_create(email=student, semester=period_obj.semester)
                UnregisteredStudent.objects.filter(email=student.email).delete()
                text = "Allocation Form filled Successfully"
            except Exception as e:
                text = "The Form is closed for now"
                print(e)
        # else:
        #     text="The Form is closed for now"
        #     print("The Form is closed for now")
    except Exception as e:
        print(e)
        text = "Signed in account can not fill the allocation form"
    context = {"text": text, "caterer_list": caterer_list, "allocation_form_details": alloc_form}
    return render(request, "allocationForm.html", context)

@login_required
def profile(request):
    """
    Display the Profile Page :model:`home.models.students`.

    **Template:**

    :template:`home/profile.html`
    """
    text = ""
    student = Student.objects.filter(email=str(request.user.email)).last()
    socialaccount_obj = SocialAccount.objects.filter(provider='google', user_id=request.user.id)
    picture = "not available"
    allocation = Allocation.objects.filter(email=student).last()
    #improve this alignment of text to be shown on the profile section
    if allocation:
        allocation_info_list = [allocation.student_id, allocation.caterer.name, str(allocation.high_tea)]
        allocation_info = "Allocation ID: " + allocation.student_id + " Caterer: " + allocation.caterer.name + " High Tea: " + str(allocation.high_tea)
    else:
        allocation_info = "Not allocated for this period"
    if len(socialaccount_obj):
            picture = socialaccount_obj[0].extra_data['picture']
    # if request.method == "POST" and request.user.is_authenticated:
    #     try:
    #         student = Student.objects.get(email=str(request.user.email))
    #         student.name = request.POST["name"]
    #         student.room_no = request.POST["room_no"]
    #         student.save()
    #         text = "Profile Updated Successfully"
    #     except:
    #         text = "Email ID does not exist in the database. Please eneter the correct email ID"
    context = {"text": text,"student":student,"picture":picture,"allocation_info":allocation_info,"allocation_info_list":allocation_info_list}
    return render(request, "profile.html", context)

@login_required
def period_data(request):
    print("period_data")
    name = request.GET.get('semester')
    if(name=="autumn22"):
        period = PeriodAutumn22.objects.all()
    elif(name=="spring23"):
        period = PeriodSpring23.objects.all()
    else:
        semester = Semester.objects.get(name=name)
        period = Period.objects.filter(semester=semester)
    period_data = {
        'semester': name,
        'data': list(period.values('Sno','start_date', 'end_date')),
    }
    # print(period_data['semester'])
    # print(period_data['data'])
    return JsonResponse(period_data)

@login_required
def rebate_data(request):
    print("rebate_data")
    user = request.user
    student = Student.objects.get(email=user.email)
    sno = request.GET.get('period')
    semester = request.GET.get('semester')
    if(semester=="autumn22"):
        rebate = RebateAutumn22.objects.filter(email=student).last()
        rebate_bills = get_rebate_bills(rebate,sno)
    elif(semester=="spring23"):
        rebate = RebateSpring23.objects.filter(email=student).last()
        rebate_bills = get_rebate_bills(rebate,sno)
    else:
        semester_obj= Semester.objects.get(name=semester)
        rebate = StudentBills.objects.filter(email=student, semester = semester_obj).last()
        rebate_bills = get_rebate_bills(rebate,sno)
    rebate_data = {
        'semester': semester,
        'period': sno,
        'data':rebate_bills
    }
    return JsonResponse(rebate_data)