from django.db import models
from django.utils.translation import gettext as _


class About(models.Model):
    # Single About on Home Page
    description = models.TextField(_("Description"))

    def __str__(self):
        return "About Us Content"
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Update(models.Model):
    # All Updates on Home Page
    update = models.CharField(_("update"), max_length=120)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Posted on " + self.time_stamp
    
    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"
