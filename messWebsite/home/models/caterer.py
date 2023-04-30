from django.db import models
from django.utils.translation import gettext as _


class Caterer(models.Model):
    """
    Stores All Caterers on cafeteria page
    """
    name = models.CharField(_("Caterer Name"), max_length=50,
                            help_text="The text in this text field contains the caterer name.")
    upper_description = models.TextField(
        _("Upper Description"), help_text="This contains the description of the respective caterer that will show on the upper side.")
    sheet_url = models.URLField(
        _("Menu URL"), help_text="This contains the google sheets url link for the respective caterers menu.")
    lower_description = models.TextField(
        _("Lower Discription"), default="", help_text="This contains the description of the respective caterer that will show on the lower side.")
    student_limit = models.IntegerField(
        _("Caterers Student Limit"), default=0, help_text="The limit on number of students it can have")

    def __str__(self):
        return "Caterer " + self.name

    class Meta:
        verbose_name = "Caterer"
        verbose_name_plural = "Caterers"
