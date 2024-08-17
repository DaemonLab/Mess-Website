from django.db import models
from django.utils.translation import gettext as _


class Form(models.Model):
    """
    Stores All forms on the links page
    """

    heading = models.CharField(
        _("Form Heading"),
        max_length=30,
        help_text="This contains the heading of the form to be added.",
    )
    description = models.CharField(
        _("Form Description"),
        max_length=120,
        help_text="This contains the description of the form to be added.",
        blank=True,
    )
    url = models.URLField(
        _("Form URL"), help_text="This contains the URL link of the form."
    )

    def __str__(self):
        return "Form " + self.heading

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
