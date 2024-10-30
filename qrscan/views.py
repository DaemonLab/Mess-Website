from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Student
from .models import MessCard
from allauth.socialaccount.models import SocialAccount

@login_required
def mess_card(request):
    """
    Display the Mess card of the user.

    *Template:*

    :template:`mess_card.html`
    """

    student = Student.objects.filter(email__iexact=str(request.user.email)).last()
    socialaccount_obj = SocialAccount.objects.filter(
        provider="google", user_id=request.user.id
    )
    allocation = student.allocation_set.last()

    if(not allocation):
        raise ValueError("Allocation not found!")
    mess_card, _ = MessCard.objects.get_or_create(student=student)

    if(not mess_card.allocation):
        setattr(mess_card, allocation)
        mess_card.save()
    elif((mess_card.allocation != allocation) and allocation.period.end_date < timezone.localtime().date()):
        setattr(mess_card, "allocation", allocation)
        mess_card.save()

    picture = "not available"
    try:
        if socialaccount_obj:
            picture = socialaccount_obj[0].extra_data["picture"]
    except (IndexError, KeyError):
        picture = "not available"

    context = {
        "student": student,
        "picture": picture,
        "user": request.user,
        "mess_card": mess_card,
    }

    return render(request, "mess_card.html", context=context)

