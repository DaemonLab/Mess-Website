from django.db import models
from django.utils.translation import gettext as _


class Rule(models.Model):
    # All Rules on Rules Page
    rule = models.TextField(_("Rule"))

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"


class Penalty(models.Model):
    # All Penalties on Rules Page
    penalty = models.TextField(_("Penalty"))

    class Meta:
        verbose_name = "Penalty"
        verbose_name_plural = "Penalties"


# will only show one value
class ShortRebate(models.Model):
    desc = models.TextField()
    link = models.URLField()
    policy = models.TextField()
    circulation = models.TextField()
    infoToCaterer = models.TextField()
    note = models.TextField()
    Memebers = models.TextField()
    biling = models.TextField()


# will show all point of long term rebate, using for loop
class LongRebate(models.Model):
    rule = models.TextField()
