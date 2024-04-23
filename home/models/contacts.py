from django.db import models
from django.utils.translation import gettext as _


class Contact(models.Model):
    """
    Stores All Contacts on Contact Page
    """
    occupation = models.TextField(_("Occupation"), 
                                  help_text="This contains the occupation of the contact to be added")
    hostel_sec = models.BooleanField(_("Dining Secretary"))
    name = models.CharField(_("Name"), max_length=30, null=True, blank=True,
                            help_text="This contains the name of the contact to be added")
    contact = models.CharField(_("Phone Number"), max_length=12, null=True, blank=True,
                               help_text="This contains phone number of the contact to be added")
    email = models.EmailField(_("Email"), 
                              help_text="This contains email of the contact to be added")

    def __str__(self):
        return "Contact of " + self.occupation

    class Meta:
        app_label = "home"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
