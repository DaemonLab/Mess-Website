from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label=_('First Name'))
    last_name = forms.CharField(max_length=30, label=_('Last Name'))
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

# class CustomSocialSignupForm(SocialSignupForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.prevent_enumeration = False