from django.db import models
from django.utils.translation import gettext as _


class Cafeteria(models.Model):
    """
    Stores all Cafeterias on cafeteria page
    """
    name = models.CharField(_("Name of Cafeteria"), max_length=30,
                            help_text="This contains the name of the cafeteria")
    poc = models.CharField(_("Point of Contact"), max_length=30,
                           help_text="This contains the name of the point of contact of the respective cafeteria")
    contact = models.CharField(_("Phone Number"), max_length=10, null=True,
                               blank=True, help_text="This contains the contact(phone number) of the POC")
    image = models.ImageField(_("Image of Cafeteria"),
                              upload_to="static/images", null=True, blank=True,)

    def __str__(self):
        return "Cafeteria " + self.name

    class Meta:
        verbose_name = "Cafeteria"
        verbose_name_plural = "Cafeterias"
