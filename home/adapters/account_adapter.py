from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model
from django.forms import ValidationError

from home.models import Student

User = get_user_model()


class CustomAccountAdapter(DefaultAccountAdapter):
    def should_send_confirmation_mail(self, request, email_address):
        return None

    def clean_email(self, email):
        RestrictedList = Student.objects.all().values_list("email")
        if email.endswith("iiti.ac.in"):
            raise ValidationError(
                "Please login with your IITI email ID through google login only."
            )
        elif RestrictedList.filter(email=email).exists():
            print(email)
            print(RestrictedList.filter(email=email))
        else:
            raise ValidationError(
                "This email ID is not registered with the Dining Facility. Please contact the Dining Wadern Office."
            )
        return email
