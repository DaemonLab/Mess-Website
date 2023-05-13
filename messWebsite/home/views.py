from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from django.core.files.storage import default_storage
from home.models import (
    About,
    Update,
    Carousel,
    Photos,
    Rule,
    ShortRebate,
    LongRebateData,
    Caterer,
    Form,
    Cafeteria,
    Contact,
    Rebate,
    Allocation,
    Student,
    RebateAutumnSem,
    RebateSpringSem,
    LongRebate,
    UnregisteredStudent
)
import pandas as pd
import datetime
import io
from django.utils.dateparse import parse_date
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    """
    Display the Home Page :model:`home.models.home`.

    **Template:**

    :template:`home/home.html`

    """
    aboutInfo = About.objects.all()
    update = Update.objects.all()
    caterer = Caterer.objects.all()
    carousel = Carousel.objects.all()
    photos = Photos.objects.all()
    context = {
        "about": aboutInfo,
        "updates": update,
        "caterer": caterer,
        "carousel": carousel,
        "photos": photos,
        'all_caterer' : Caterer.objects.all()
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
    LongRebates = LongRebateData.objects.all()
    form = Form.objects.all()
    params = {
        "rule": rules,
        "shortRebate": shortRebates,
        "longRebate": LongRebates,
        "form": form,
    }

    return render(request, "rules.html", params)


def caterer(request, name):
    """
    Display the Caterer Page :model:`home.models.caterer`.

    **Template:**

    :template:`home/caterer.html`

    """
    caterer = Caterer.objects.get(name=name)
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


def count(start, end):
    """Counts the number of days of rebate applied"""
    sum = ((end - start).days) + 1
    return sum


def is_present_autumn(s):
    """
    Checks if student is registered in the rebate bills of autumn semester,
    if not the function registers it with that email ID
    """
    try:
        student = RebateAutumnSem.objects.get(email=str(s.email))
    except:
        print(Exception)
        student = RebateAutumnSem(email=str(s.email))
        student.save()
    return student


def is_present_spring(s):
    """
    Checks if student is registered in the rebate bills of spring semester,
    if not the function registers it with that email ID
    """
    try:
        student = RebateSpringSem.objects.get(email=str(s.email))
    except:
        print(Exception)
        print(2)
        student = RebateSpringSem(email=str(s.email))
        student.save()
    return student


def check(a, s, start, end, month):
    """
    Checks what month rebate is being applied,
    if the rebate doesnot exceeds 8 days for that month approves the rebate and
    adds the rebate to rebate bills
    """
    match month:
        case "January":
            student = is_present_spring(s)
            sum = count(start, end)
            if student.januaryShort + sum <= 8:
                # student.january+=sum
                # student.highTeaJanuary = a.high_tea
                # student.save(update_fields=["january", "highTeaJanuary"])
                return -1
            if start.month == 1 and end.month == 1:
                return -2
            else:
                return 8 - student.januaryShort
        case "Feburary":
            student = is_present_spring(s)
            sum = count(start, end)
            if student.feburaryShort + sum <= 8:
                # student.feburary+=sum
                # student.highTeaFeburary = a.high_tea
                # student.save(update_fields=["feburary", "highTeaFeburary"])
                return -1
            elif start.month != 2 and end.month != 2:
                return -2
            else:
                return 8 - student.feburaryShort
        case "March":
            student = is_present_spring(s)
            sum = count(start, end)
            if student.march + sum <= 8:
                # student.march+=sum
                # student.highTeaMarch = a.high_tea
                # student.save(update_fields=["march", "highTeaMarch"])
                return -1
            elif start.month != 3 and end.month != 3:
                return -2
            else:
                return 8 - student.marchShort
        case "April":
            student = is_present_spring(s)
            sum = count(start, end)
            if sum + student.april <= 8:
                # student.april+=sum
                # student.highTeaApril = a.high_tea
                # student.save(update_fields=["april", "highTeaApril"])
                return -1
            elif start.month != 4 and end.month != 4:
                return -2
            else:
                return 8 - student.aprilShort
        case "May":
            student = is_present_spring(s)
            sum = count(start, end)
            if sum + student.mayShort <= 8:
                # student.may+=sum
                # student.highTeaMay = a.high_tea
                # student.save(update_fields=["may", "highTeaMay"])
                return -1
            elif start.month != 5 and end.month != 5:
                return -2
            else:
                return 8 - student.mayShort
        case "June":
            student = is_present_spring(s)
            sum = count(start, end)
            if student.june + sum <= 8:
                # student.june+=sum
                # student.highTeaJune = a.high_tea
                # student.save(update_fields=["june", "highTeaJune"])
                return -1
            elif start.month != 6 and end.month != 6:
                return -2
            else:
                return 8 - student.juneShort
        case "July":
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.july + sum <= 8:
                # student.july+=sum
                # student.highTeaJuly = a.high_tea
                # student.save(update_fields=["july", "highTeaJuly"])
                return -1
            elif start.month != 7 and end.month != 7:
                return -2
            else:
                return 8 - student.julyShort
        case "August":
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.august + sum <= 8:
                # student.august+=sum
                # student.highTeaAugust = a.high_tea
                # student.save(update_fields=["august", "highTeaAugust"])
                return -1
            elif start.month != 8 and end.month != 8:
                return -2
            else:
                return 8 - student.augustShort
        case "September":
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.september + sum <= 8:
                # student.september+=sum
                # student.highTeaSeptember = a.high_tea
                # student.save(update_fields=["september", "highTeaSeptember"])
                return -1
            elif start.month != 9 and end.month != 9:
                return -2
            else:
                return 8 - student.septemberShort
        case "October":
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.october + sum <= 8:
                # student.october+=sum
                # student.highTeaOctober = a.high_tea
                # student.save(update_fields=["october", "highTeaOctober"])
                return -1
            elif start.month != 10 and end.month != 10:
                return -2
            else:
                return 8 - student.octoberShort
        case "November":
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.november + sum <= 8:
                # student.november+=sum
                # student.highTeaNovember = a.high_tea
                # student.save(update_fields=["november", "highTeaNovember"])
                return -1
            elif start.month != 11 and end.month != 11:
                return -2
            else:
                return 8 - student.novemberShort
        case "December":
            student = is_present_autumn(s)
            sum = count(start, end)
            if student.december + sum <= 8:
                # student.december+=sum
                # student.highTeaDecember = a.high_tea
                # student.save(update_fields=["december", "highTeaDecember"])
                return -1
            elif start.month != 12 and end.month != 12:
                return -2
            else:
                return 8 - student.decemberShort
        # case default:
        #     return "something"


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
        allocation_id = Allocation.objects.get(roll_no__email=str(request.user.email))
        key = str(allocation_id.student_id)
    except Allocation.DoesNotExist:
        key = "Signed in account does not does not have any allocation ID"
    except Allocation.MultipleObjectsReturned:
        allocation_id = Allocation.objects.filter(
            roll_no__email=str(request.user.email)
        ).last()
        key = str(allocation_id.student_id)
    if request.method == "POST" and request.user.is_authenticated:
        try:
            start_date = parse_date(request.POST["start_date"])
            end_date = parse_date(request.POST["end_date"])
            if start_date.month == end_date.month:
                diff = ((end_date - start_date).days) + 1
                diff2 = (start_date - datetime.date.today()).days
                try:
                    # Allocation.objects.filter(
                    #     student_id=request.POST["allocation_id"]
                    # ).last()
                    try:
                        # allocation = Allocation.objects.get(
                        #     roll_no__email=str(request.user.email),
                        #     student_id=request.POST["allocation_id"],
                        # )
                        student = Student.objects.filter(
                            email=str(request.user.email)
                        ).first()
                        month = allocation_id.month
                        print(month)
                        ch = check(allocation_id, student, start_date, end_date, month)
                        if ch == -2:
                            text = "Please fill the rebate of this month only"
                        elif ch >= 0:
                            text = (
                                "You can only apply for max 8 days in a month. Days left for this month: "
                                + str(ch)
                            )
                        else:
                            if (diff) <= 7 and diff >= 2 and diff2 >= 2:
                                r = Rebate(
                                    email=request.user.email,
                                    allocation_id=allocation_id,
                                    start_date=request.POST["start_date"],
                                    end_date=request.POST["end_date"],
                                    approved=False,
                                )
                                r.save()
                                text = "You have successfully submitted the form, subject to approval of Office of Dining Warden. Thank You!"
                            elif 0 < diff < 2:
                                text = "Min no of days for rebate is 2"
                            elif diff2 < 2:
                                text = "Form needs to be filled atleast 2 days prior the comencement of leave."
                            elif diff > 7:
                                text = "Max no of days for rebate is 7"
                            elif diff < 0:
                                text = "Please enter the correct dates"
                            else:
                                text = "Your rebate application has been rejected due to non-compliance of the short term rebate rules"
                    except Allocation.DoesNotExist:
                        text = "Email ID does not match with the allocation ID"
                except Allocation.DoesNotExist:
                    text = " The asked allocation ID does not exist. Please enter the correct ID."
            else:
                text = "Please enter the rebate dates within this month only"
        except Exception as e:
            print(e)
            text = "Invalid Dates filled"
    context = {"text": text, "key": key, "list": list}
    return render(request, "rebateForm.html", context)


def allocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/allocation.html`

    Gets the data from the allocation csv,
    parses each row and allocates each student an allocation ID and caterer for that month.
    Which can be then exported in the admin page.
    CSV should be imported from /allocation/ url only
    Allocation data should only be filled 2 days prior to the next month
    This form can only be accessed by the Institute's admin
    """
    messages = ""
    if (
        request.method == "POST"
        and request.user.is_authenticated
        and request.user.is_staff
    ):
        csv = request.FILES["csv"]
        csv_data = pd.read_csv(io.StringIO(csv.read().decode("utf-8")))
        print(csv_data.head())

        for record in csv_data.to_dict(orient="records"):
            try:
                first_pref = str(record["first_pref"]).capitalize()
                second_pref = str(record["second_pref"]).capitalize()
                third_pref = str(record["third_pref"]).capitalize()
                month = str(record["month"]).capitalize()
                high_tea = record["high_tea"]
                r = Student.objects.filter(email=record["email"]).first()
                print(r)
                print("hi1")
                for pref in [first_pref, second_pref, third_pref]:
                    kanaka = Caterer.objects.get(name="Kanaka")
                    ajay = Caterer.objects.get(name="Ajay")
                    gauri = Caterer.objects.get(name="Gauri")
                    if pref == kanaka.name and kanaka.student_limit > 0:
                        student_id = str(kanaka.name[0])
                        if high_tea == True:
                            student_id += "H"
                        student_id += str(kanaka.student_limit)
                        caterer_name = kanaka.name
                        kanaka.student_limit -= 1
                        kanaka.save(update_fields=["student_limit"])
                        break
                    elif pref == ajay.name and ajay.student_limit > 0:
                        student_id = str(ajay.name[0])
                        if high_tea == True:
                            student_id += "H"
                        student_id += str(ajay.student_limit)
                        caterer_name = ajay.name
                        ajay.student_limit -= 1
                        ajay.save(update_fields=["student_limit"])
                        break
                    elif pref == gauri.name and gauri.student_limit > 0:
                        student_id = str(gauri.name[0])
                        if high_tea == True:
                            student_id += "H"
                        student_id += str(gauri.student_limit)
                        caterer_name = gauri.name
                        gauri.student_limit -= 1
                        gauri.save(update_fields=["student_limit"])
                        break
                a = Allocation(
                    roll_no=r,
                    student_id=student_id,
                    month=month,
                    caterer_name=caterer_name,
                    high_tea=high_tea,
                    first_pref=first_pref,
                    second_pref=second_pref,
                    third_pref=third_pref,
                )
                a.save()
                UnregisteredStudent.objects.filter(email=r.email).delete()
            except Exception as e:
                print(e)
        messages = "Form submitted. Please check the admin page."
    Ajay_high_tea = Allocation.objects.filter(caterer_name="Ajay", high_tea=True).count()
    Gauri_high_tea = Allocation.objects.filter(caterer_name="Gauri", high_tea=True).count()
    Kanaka_high_tea = Allocation.objects.filter(caterer_name="Kanaka", high_tea=True).count()
    Ajay_total = Allocation.objects.filter(caterer_name="Ajay").count()
    Gauri_total = Allocation.objects.filter(caterer_name="Gauri").count()
    Kanaka_total = Allocation.objects.filter(caterer_name="Kanaka").count()
    Ajay_left = Caterer.objects.get(name="Ajay").student_limit
    Gauri_left = Caterer.objects.get(name="Gauri").student_limit
    Kanaka_left = Caterer.objects.get(name="Kanaka").student_limit
    caterer_list = [["Ajay",Ajay_high_tea,Ajay_total,Ajay_left], ["Gauri",Gauri_high_tea,Gauri_total,Gauri_left], ["Kanaka", Kanaka_high_tea,Kanaka_total,Kanaka_left]]
    context = {"messages": messages,"list": caterer_list}
    return render(request, "admin/allocation.html", context)


def addAllocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/addAllocation.html`

    Gets the data from the allocation form , and
    allocates an allocation ID and caterer for that month corresponding to the student with submitted email ID.
    This is for students who did not filled the allocation form
    Allocation data should only be filled 2 days prior to the next month
    This form can only be accessed by the Institute's admin
    """
    text = ""
    all_caterers = Caterer.objects.all()
    available_caterer = []
    for caterer in all_caterers:
        current = Caterer.objects.get(name=caterer.name)
        if current.student_limit > 0:
            available_caterer.append(current.name)
    if (
        request.method == "POST"
        and request.user.is_authenticated
        and request.user.is_staff
    ):
        csv = request.FILES["csv"]
        csv_data = pd.read_csv(io.StringIO(csv.read().decode("utf-8")))
        print(csv_data.head())

        for record in csv_data.to_dict(orient="records"):
            try:
                student= Student.objects.get(email=record["email"])
                high_tea=False
                caterer = available_caterer[0]
                month = str(record["month"]).capitalize()
                if(caterer=="Kanaka"):
                    kanaka = Caterer.objects.get(name="Kanaka")
                    student_id = str(kanaka.name[0])
                    student_id += str(kanaka.student_limit)
                    kanaka.student_limit -= 1
                    kanaka.save(update_fields=["student_limit"])
                elif(caterer=="Ajay"):
                    ajay = Caterer.objects.get(name="Ajay")
                    student_id = str(ajay.name[0])
                    student_id += str(ajay.student_limit)
                    ajay.student_limit -= 1
                    ajay.save(update_fields=["student_limit"])
                elif(caterer=="Gauri"):
                    gauri = Caterer.objects.get(name="Gauri")
                    student_id = str(gauri.name[0])
                    student_id += str(gauri.student_limit)
                    gauri.student_limit -= 1
                    gauri.save(update_fields=["student_limit"])
                a = Allocation(
                    roll_no=student,
                    student_id=student_id,
                    month=month,
                    caterer_name=caterer,
                    high_tea=high_tea,
                    first_pref=caterer,
                    second_pref=caterer,
                    third_pref=caterer,
                )
                a.save()
                UnregisteredStudent.objects.filter(email=student.email).delete()
            except Exception as e:
                print(e)
                print(12121)
    context = {"text": text, "caterers": available_caterer}
    return render(request, "admin/addAllocation.html", context)


def addLongRebateBill(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/longRebate.html`

    Gets the data from the log term rebate form , and adds it to the coresponding rebate bill
    This form can only be accessed by the Institute's admin
    """
    text = ""
    try:
        allocation_id = Allocation.objects.get(roll_no__email=str(request.user.email))
        key = str(allocation_id.student_id)
    except Allocation.DoesNotExist:
        key = "Signed in account does not does not have any allocation ID"
    except Allocation.MultipleObjectsReturned:
        allocation_id = Allocation.objects.filter(
            roll_no__email=str(request.user.email)
        ).last()
        key = str(allocation_id.student_id)
    if request.method == "POST" and request.user.is_authenticated:
        try:
            start_date = parse_date(request.POST["start_date"])
            end_date = parse_date(request.POST["end_date"])
            days = (end_date - start_date).days + 1
            try:
                file=request.FILES["pdf"]
                print(file)
                long = LongRebate(
                    email=request.user.email,
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
    context = {"text": text, "key": key}
    return render(request, "longRebate.html", context)
