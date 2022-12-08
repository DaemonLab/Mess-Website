from django.db import models
from django.utils.translation import gettext as _


class Contact(models.Model):
    # All Contacts on Contact Page
    occupation = models.CharField(_("Occupation"), max_length=5)
    hostel_sec = models.BooleanField(_("Dining Secretary"))
    name = models.CharField(_("Name"), max_length=30, null=True, blank=True)
    contact = models.CharField(_("Phone Number"), max_length=10, null=True, blank=True)
    email = models.EmailField(_("Email"))

    def __str__(self):
        return "Contact of " + self.occupation

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
