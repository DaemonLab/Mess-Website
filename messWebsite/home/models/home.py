from django.db import models
from django.utils.translation import gettext as _


class About(models.Model):
    # Single About on Home Page
    description = models.TextField(_("Description"),help_text="The text added in this text field will show up in the about section of the home page.")

    def __str__(self):
        return "About Us Content"
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Update(models.Model):
    # All Updates on Home Page
    update = models.CharField(_("update"), max_length=120,help_text="The text added in this text field will show as one of the update in the update section")
    time_stamp = models.DateTimeField(auto_now_add=True,help_text="time stamp of the update will also show up on the page and this also decides the order of the updates that show up")

    def __str__(self):
        return "Posted on " + self.time_stamp.strftime("%m/%d/%Y, %H:%M:%S")
    
    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"
