from django.db import models
from django.utils.translation import gettext as _


class Cafeteria(models.Model):
    """
    Stores all shops on Additional Services page
    """
    name = models.CharField(_("Name of Service"), max_length=30,
                            help_text="This contains the name of the Service")
    poc = models.CharField(_("Point of Contact"), max_length=30,
                           help_text="This contains the name of the point of contact of the respective Service")
    contact = models.CharField(_("Phone Number"), max_length=10, null=True,
                               blank=True, help_text="This contains the contact(phone number) of the POC")
    image = models.ImageField(_("Image of Service"),
                              upload_to="static/images", null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "home"
        verbose_name = "Additional Services"
        verbose_name_plural = "Additional Services"
