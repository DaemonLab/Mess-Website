from django.db import models
from django.utils.translation import gettext as _

class Cafeteria(models.Model):
    # All Cafeterias on cafeteria page
    name = models.CharField(_("Name of Cafeteria"), max_length=30)
    poc = models.CharField(_("Point of Contact"), max_length=30)
    contact = models.CharField(_("Phone Number"), max_length=10, null=True, blank=True)

    def __str__(self):
        return "Cafeteria " + self.name
    
    class Meta:
        verbose_name = "Cafeteria"
        verbose_name_plural = "Cafeterias"
