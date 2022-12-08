from django.db import models
from django.utils.translation import gettext as _


class Caterer(models.Model):
    # All Caterers on Caterers Page
    name = models.CharField(_("Caterer Name"), max_length=50)
    upper_description = models.TextField(_("Upper Description"))
    sheet_url = models.URLField(_("Menu URL"))
    lower_description = models.TextField(_("Lower Discription"))

    def __str__(self):
        return "Caterer " + self.name

    class Meta:
        verbose_name = "Caterer"
        verbose_name_plural = "Caterers"
