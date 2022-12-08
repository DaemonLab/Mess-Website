from django.db import models
from django.utils.translation import gettext as _

class Form(models.Model):
    # All forms on the links page
    heading = models.CharField(_("From Heading"), max_length=30)
    description = models.CharField(_("Form Description"), max_length=120)
    url = models.URLField(_("Form URL"))

    def __str__(self):
        return "Form " + self.heading

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
