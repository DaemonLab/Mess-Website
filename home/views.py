import logging
from datetime import date, timedelta

from allauth.socialaccount.models import SocialAccount
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_date
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.timezone import now

from home.models import (
    About,
    Allocation,
    AllocationForm,
    Cafeteria,
    Carousel,
    Caterer,
    Contact,
    Form,
    LeftShortRebate,
    LongRebate,
    Period,
    Rebate,
    Rule,
    Semester,
    ShortRebate,
    Student,
    StudentBills,
    UnregisteredStudent,
    Update,
)

from .utils.get_rebate_bills import get_rebate_bills
from .utils.rebate_checker import is_not_duplicate, max_days_rebate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    """
    Display the Home Page :model:`home.models.home`.

    *Template:*

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
        "all_caterer": caterer,
    }
    return render(request, "home.html", context)


def rules(request):
    """
    Display the Rules Page :model:`home.models.rules`.

    *Template:*

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

    *Template:*

    :template:`home/caterer.html`

    """
    caterer = Caterer.objects.get(name=name, visible=True)
    context = {"caterer": caterer}
    return render(request, "caterer.html", context)


def links(request):
    """
    Display the Forms Page :model:`home.models.links`.

    *Template:*

    :template:`home/links.html`

    """
    form = Form.objects.all()
    context = {"form": form}
    return render(request, "links.html", context)


def cafeteria(request):
    """
    Display the Cafeteria Page :model:`home.models.cafeteria`.

    *Template:*

    :template:`home/cafeteria.html`

    """
    cafeteria = Cafeteria.objects.all()
    context = {"cafeteria": cafeteria}
    return render(request, "cafeteria.html", context)


def contact(request):
    """
    Display the Contact Page :model:`home.models.contacts`.

    *Template:*

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

    *Template:*

    :template:`rebateForm.html`
    """
    message = ""
    period_obj = None
    allocation = None
    try:
        student = Student.objects.get(email__iexact=request.user.email)
        if not student.allocation_enabled:
            message = "You are not eligible to apply for short rebate. For more details, please inquire at the Dining Office."
            return render(request, "rebateForm.html", {"text": message})
    except Student.DoesNotExist:
        message = "Signed in account does not have any allocation ID"
        return render(request, "rebateForm.html", {"text": message})

    try:
        period_obj = next(
            period
            for period in Period.objects.all()
            if period.end_date > date.today() + timedelta(1)
        )
        allocation = Allocation.objects.get(
            email__iexact=request.user.email, period=period_obj
        )
    except Exception as e:
        logger.error(e)
        message = "You are not allocated for current period, please contact the dining warden to allocate you to a caterer"
    if request.method == "POST" and request.user.is_authenticated:
        if not period_obj or not allocation:
            message = "You are not allocated for current period, please contact the dining warden to allocate you to a caterer"
            request.session["text"] = message
            return redirect(request.path)

        try:
            start_date = parse_date(request.POST["start_date"])
            end_date = parse_date(request.POST["end_date"])
            rebate_days = ((end_date - start_date).days) + 1
            before_rebate_days = (start_date - date.today()).days

            if rebate_days > 7:
                message = "Max no of days for rebate is 7"
            elif before_rebate_days < 2:
                message = "Form needs to be filled atleast 2 days prior the comencement of leave."
            elif not is_not_duplicate(student, start_date, end_date):
                message = "You have already applied for rebate during this duration"
            elif 0 < rebate_days < 2:
                message = "Min no of days for rebate is 2"
            else:
                additional_message = ""
                if not period_obj.start_date <= start_date <= period_obj.end_date:
                    short_left_rebate = LeftShortRebate(
                        email=student.email,
                        start_date=start_date,
                        end_date=end_date,
                        date_applied=date.today(),
                    )
                    short_left_rebate.save()
                    message = "You have successfully submitted the rebate, it will get added to your bills in the next period."
                    upper_cap_check = -1
                elif not period_obj.start_date <= end_date <= period_obj.end_date:
                    short_left_rebate = LeftShortRebate(
                        email=student.email,
                        start_date=period_obj.end_date + timedelta(days=1),
                        end_date=end_date,
                        date_applied=date.today(),
                    )
                    end_date = period_obj.end_date
                    upper_cap_check = max_days_rebate(
                        student, start_date, period_obj.end_date, period_obj
                    )
                    if upper_cap_check < 0:
                        short_left_rebate.save()
                        additional_message = " Note: The days after the current period end date will be added to your bills in the next period."
                else:
                    upper_cap_check = max_days_rebate(
                        student, start_date, end_date, period_obj
                    )
                if upper_cap_check >= 0:
                    message = (
                        "You can only apply for max 8 days in a period. Days left for this period: "
                        + str(upper_cap_check)
                    )
                elif not message:
                    rebate = Rebate(
                        email=student,
                        allocation_id=allocation,
                        start_date=start_date,
                        end_date=end_date,
                        approved=True,
                    )
                    rebate.save()
                    message = "You have successfully submitted the rebate. Thank You! You shall recieve a confirmation mail, If not please contact the Dining Warden."
                    if additional_message:
                        message += additional_message
                elif not message:
                    message = "Your rebate application has been rejected due to non-compliance of the short term rebate rules"
        except Exception as e:
            logger.error(e)
            message = (
                "Ohh No! an unknown ERROR occured, Please inform about it immediatly to the Dining Wadern. Possible Error: "
                + str(e)
            )
        request.session["text"] = message
        return redirect(request.path)
    text = request.session.get("text", "")
    if text != "":
        del request.session["text"]
    if not allocation:
        context = {"text":text}
    else:
        context = {"text": text, "key": allocation.student_id}
    return render(request, "rebateForm.html", context)


@staff_member_required(redirect_field_name="/", login_url="/")
def allocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    *Template:*

    :template:`home/allocation.html`

    This form can only be accessed by the Institute's admin
    """
    period_obj = Period.objects.filter().last()
    caterer_list = []
    for caterer in Caterer.objects.filter(visible=True).all():
        caterer_high_tea = Allocation.objects.filter(
            caterer=caterer, high_tea=True, period=period_obj
        ).count()
        caterer_total = Allocation.objects.filter(
            caterer=caterer, period=period_obj
        ).count()
        caterer_left = caterer.student_limit
        caterer_list.append(
            [caterer.name, caterer_high_tea, caterer_total, caterer_left]
        )
    context = {"list": caterer_list}
    return render(request, "admin/allocation.html", context)


@login_required
def addLongRebateBill(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    *Template:*

    :template:`home/longRebate.html`

    Gets the data from the long-term rebate form and adds it to the corresponding rebate bill.
    This form can only be accessed by the Institute's admin.
    """
    text = ""
    try:
        student = Student.objects.get(email__iexact=request.user.email)
        if not student.allocation_enabled:
            text = "You are not eligible to apply for long rebate. For more details, please inquire at the Dining Office."
    except Student.DoesNotExist:
        text = "Email ID does not exist in the database. Please log in using the correct email ID."
        return render(request, "longRebate.html", {"text": text})

    if request.method == "POST" and request.user.is_authenticated:
        try:
            start_date = parse_date(request.POST["start_date"])
            end_date = parse_date(request.POST["end_date"])
            before_rebate_days = (start_date - date.today()).days
            days = (end_date - start_date).days + 1

            if not is_not_duplicate(student, start_date, end_date):
                text = "You have already applied for rebate for these dates"
            elif before_rebate_days < 2:
                text = "Your start date has to be 2 days from today's date"
            elif days < 0:
                text = "Your end date should be after your start date"
            else:
                try:
                    file = request.FILES["img"]
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
                    text = "An error occurred while processing your form submission. If you're submitting an application, try compressing it before resubmitting. If the issue persists, please report it to the admin."
                    logger.error(e)
        except Exception as e:
            logger.error(e)
            text = "An unexpected error occurred. Please try again later."

        request.session["text"] = text
        return redirect(request.path)

    text = request.session.get("text", text)
    if "text" in request.session:
        del request.session["text"]

    context = {"text": text}
    return render(request, "longRebate.html", context)



@login_required
def allocationForm(request):
    """
    Display the Allocation Form Page :model:`home.models.students`.

    *Template:*

    :template:`home/allocationForm.html`

    Gets the data from the allocation form, and adds it to the corresponding allocation model
    """
    caterer_list = Caterer.objects.filter(visible=True).all()
    alloc_form = AllocationForm.objects.filter(active=True).last()
    text = ""
    message = ""

    if not alloc_form:
        message = "Form is closed for now"
    else:
        student = Student.objects.filter(email__iexact=str(request.user.email)).last()
        if not student:
            message = "Signed in account cannot fill the allocation form. Please inform the dining Office to add your email ID to the database"
        elif not student.allocation_enabled: 
            message = "You are not eligible to fill out this allocation form. For more details, please inquire at the Dining Office."
        elif (alloc_form.start_time and alloc_form.start_time > now()) or (
            alloc_form.end_time and alloc_form.end_time < now()
        ):
            message = "The Form is closed for now"
        elif Allocation.objects.filter(
            email=student, period=alloc_form.period
        ).exists():
            message = "You have filled the form for this period. Please visit the profile page after the allocation process is completed to check your allocated caterer"
        elif request.method == "POST" and request.user.is_authenticated:
            period_obj = alloc_form.period
            jain = request.POST["jain"] == "True"
            caterer_prefs = [
                request.POST.get(pref)
                for pref in ["first_pref", "second_pref", "third_pref"]
            ]
            caterer_prefs = [
                Caterer.objects.get(name=pref) for pref in caterer_prefs if pref
            ]

            caterer = next(
                (
                    c
                    for c in caterer_prefs
                    if c.student_limit
                    > Allocation.objects.filter(caterer=c, period=period_obj).count()
                ),
                None,
            )
            if caterer:
                student_id = (
                    f"{caterer.name[0]}{'J' if jain else ''}{caterer.student_limit}"
                )
                allocation = Allocation(
                    email=student,
                    student_id=student_id,
                    period=period_obj,
                    caterer=caterer,
                    high_tea=False,
                    jain=jain,
                    first_pref=caterer_prefs[0].name if caterer_prefs else None,
                    second_pref=(
                        caterer_prefs[1].name if len(caterer_prefs) > 1 else None
                    ),
                    third_pref=(
                        caterer_prefs[2].name if len(caterer_prefs) > 2 else None
                    ),
                )
                allocation.save()
                UnregisteredStudent.objects.filter(email__iexact=student.email).delete()
                text = "Allocation Form filled Successfully"
                request.session["text"] = text
                if url_has_allowed_host_and_scheme(request.path, allowed_hosts=None):
                    return redirect(request.path)
                else:
                    return redirect("/")
            else:
                message = "No caterer available with sufficient student limit"

    text = request.session.get("text", "")
    if text:
        del request.session["text"]

    context = {
        "text": text,
        "caterer_list": caterer_list,
        "allocation_form_details": alloc_form,
        "message": message,
    }
    return render(request, "allocationForm.html", context)


@login_required
def profile(request):
    """
    Display the Profile Page :model:`home.models.students`.

    *Template:*

    :template:`home/profile.html`
    """
    text = ""
    student = Student.objects.filter(email__iexact=str(request.user.email)).last()
    socialaccount_obj = SocialAccount.objects.filter(
        provider="google", user_id=request.user.id
    )
    picture = "not available"
    allocation: Allocation | None = Allocation.objects.filter(email=student).last()
    show_allocated_enabled = False
    if allocation and allocation.period:
        show_allocated_enabled = AllocationForm.objects.filter(
            show_allocated=True, period=allocation.period
        ).exists()
    allocation_info = {}
    # improve this alignment of text to be shown on the profile section
    if allocation and show_allocated_enabled:
        allocation_info = {
            "start date": allocation.period.start_date,
            "end date": allocation.period.end_date,
            # "Allocation ID": allocation.student_id,
            "Caterer": allocation.caterer.name,
            # "High Tea": "Yes" if allocation.high_tea else "No",
            "Jain": "Yes" if allocation.jain else "No",
        }
    try:
        if socialaccount_obj:
            picture = socialaccount_obj[0].extra_data["picture"]
        else:
            picture = "not available"
    except (IndexError, KeyError):
        picture = "not available"
    semesters = Semester.objects.all()
    context = {
        "text": text,
        "student": student,
        "picture": picture,
        "allocation_info": allocation_info,
        "semesters": semesters,
    }
    return render(request, "profile.html", context)


@login_required
def period_data(request):
    print("period_data")
    name = request.GET.get("semester")
    semester = Semester.objects.get(name=name)
    period = Period.objects.filter(semester=semester)
    period_data = {
        "semester": name,
        "data": list(period.values("Sno", "start_date", "end_date")),
    }
    return JsonResponse(period_data)


@login_required
def rebate_data(request):
    print("rebate_data")
    user = request.user
    student = Student.objects.get(email__iexact=user.email)
    sno = request.GET.get("period")
    semester = request.GET.get("semester")
    semester_obj = Semester.objects.get(name=semester)
    rebate = StudentBills.objects.filter(email=student, semester=semester_obj).last()
    if not rebate:
        return JsonResponse({"semester": semester, "period": sno, "data": []})
    rebate_bills = get_rebate_bills(rebate, sno)
    rebate_data = {"semester": semester, "period": sno, "data": rebate_bills}
    return JsonResponse(rebate_data)
