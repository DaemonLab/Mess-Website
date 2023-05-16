from django.db import models
from django.utils.translation import gettext as _


class Rule(models.Model):
    """
    Stores All Rules on the Rules Page
    """
    sno = models.AutoField(primary_key=True)
    rule = models.TextField(
        _("Rule"), help_text="The text in the text field contains the rule that will show as one of the rules of the rule page.")
    # desc = models.TextField(_("Description"),help_text="The text in the text field contains the description of the mentioned rules.")

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"



class ShortRebate(models.Model):
    """
    Stores the Short term rebate info on the rules page
    """
    desc = models.TextField(
        _("Description"), help_text="The text in the text field contains the description of the short rebate.")

    def __str__(self):
        return "Short Rebate Content"

    class Meta:
        verbose_name = "Short Rebate"
        verbose_name_plural = "Short Rebate"


