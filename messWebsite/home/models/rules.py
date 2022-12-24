from django.db import models
from django.utils.translation import gettext as _


class Rule(models.Model):
    # All Rules on Rules Page
    sno = models.AutoField(primary_key=True)
    rule = models.TextField(_("Rule"),help_text="The text in the text field contains the rule that will show as one of the rules of the rule page.")

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"


class Penalty(models.Model):
    # All Penalties on Rules Page
    penalty = models.TextField(_("Penalty"),help_text="The text in the text field contains the penalty that will show as one of the penalties of the rule page.")

    class Meta:
        verbose_name = "Penalty"
        verbose_name_plural = "Penalties"


# will only show one value
class ShortRebate(models.Model):
    desc = models.TextField(_("Description"),help_text="The text in the text field contains the description of the short rebate.")
    link = models.URLField(_("Link"),help_text="The link in this field contains the link of the short rebate google form.")
    policy = models.TextField(_("Policy"),help_text="The text in the text field contains the policies of the short rebate.")
    circulation = models.TextField(_("Circulation"),help_text="The text in the text field contains the circulation text of the short rebate form.")
    infoToCaterer = models.TextField(_("Info to the Caterer"),help_text="The text in the text field contains the information to the caterers for the short rebate form.")
    note = models.TextField(_("Note"),help_text="The text in the text field contains the note for the short rebate form.")
    Memebers = models.TextField(_("Members"),help_text="The text in the text field contains the names of the members that will handle the short rebate.")
    biling = models.TextField(_("bilings"),help_text="The text in the text field contains the billing description for the short rebate.")

    def __str__(self):
        return "Short Rebate Content"

    class Meta:
        verbose_name = "Short Rebate"
        verbose_name_plural = "Short Rebate"


# will show all point of long term rebate, using for loop
class LongRebate(models.Model):
    rule = models.TextField(_("Rule"),help_text="The text in the text field contains the rule that will show as one of the long rebate rules of the rule page.")

    class Meta:
        verbose_name = "Long Rebate"
        verbose_name_plural = "Long Rebates"