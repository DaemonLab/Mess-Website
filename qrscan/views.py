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
    mess_card = MessCard.objects.filter(student=student).last()
    print(mess_card.qr_code.path)
    picture = "not available"

    try:
        if socialaccount_obj:
            picture = socialaccount_obj[0].extra_data["picture"]
        else:
            picture = "not available"
    except (IndexError, KeyError):
        picture = "not available"

    context = {
        "student": student,
        "picture": picture,
        "user": request.user,
        "mess_card": mess_card,
    }

    return render(request, "mess_card.html", context=context)

