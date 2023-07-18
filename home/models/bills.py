from django.db import models
from django.utils.translation import gettext as _

from .allocation import Semester
from .caterer import Caterer
from .students import Student


class StudentBills(models.Model):
    """
    Storing the Rebate Bills of the Students for the Semesters
    """
    email = models.ForeignKey(Student, on_delete=models.SET_NULL, default="", null=True)
    semester = models.ForeignKey(Semester, verbose_name=_("Semester"), on_delete=models.CASCADE,null=True, default=None)
    
    period1_short = models.IntegerField(_("Period 1 Short"),default=0, null=True)
    period1_long = models.IntegerField(_("Period 1 Long"),default=0,null=True)
    period1_high_tea = models.BooleanField(_("Period 1 High Tea"),default=True, null=True)
    period1_bill = models.IntegerField(_("Period 1 Rebate Amount"),default=0, null=True)

    period2_short = models.IntegerField(_("Period 2 Short"),default=0, null=True)
    period2_long = models.IntegerField(_("Period 2 Long"),default=0,null=True)
    period2_high_tea = models.BooleanField(_("Period 2 High Tea"),default=True, null=True)
    period2_bill = models.IntegerField(_("Period 2 Rebate Amount"),default=0, null=True)

    period3_short = models.IntegerField(_("Period 3 Short"),default=0, null=True)
    period3_long = models.IntegerField(_("Period 3 Long"),default=0,null=True)
    period3_high_tea = models.BooleanField(_("Period 3 High Tea"),default=True, null=True)
    period3_bill = models.IntegerField(_("Period 3 Rebate Amount"),default=0, null=True)

    period4_short = models.IntegerField(_("Period 4 Short"),default=0, null=True)
    period4_long = models.IntegerField(_("Period 4 Long"),default=0,null=True)
    period4_high_tea = models.BooleanField(_("Period 4 High Tea"),default=True, null=True)
    period4_bill = models.IntegerField(_("Period 4 Rebate Amount"),default=0, null=True)

    period5_short = models.IntegerField(_("Period 5 Short"),default=0, null=True)
    period5_long = models.IntegerField(_("Period 5 Long"),default=0,null=True)
    period5_high_tea = models.BooleanField(_("Period 5 High Tea"),default=True, null=True)
    period5_bill = models.IntegerField(_("Period 5 Rebate Amount"),default=0, null=True)

    period6_short = models.IntegerField(_("Period 6 Short"),default=0, null=True)
    period6_long = models.IntegerField(_("Period 6 Long"),default=0,null=True)
    period6_high_tea = models.BooleanField(_("Period 6 High Tea"),default=True, null=True)
    period6_bill = models.IntegerField(_("Period 6 Rebate Amount"),default=0, null=True)

    def __str__(self):
        return str(self.email.email)

    class Meta:
        verbose_name = "Rebate Bill"
        verbose_name_plural = "Rebate Bills"

class CatererBills(models.Model):
    """
    Storing the Bills of the Caterers for the Semesters
    """
    caterer = models.ForeignKey(Caterer,on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, verbose_name=_("Semester"), on_delete=models.CASCADE,null=True, default=None)

    period1_bills = models.IntegerField(_("Period 1 Bill"),default=0, null=True)
    period2_bills = models.IntegerField(_("Period 2 Bill"),default=0, null=True)
    period3_bills = models.IntegerField(_("Period 3 Bill"),default=0, null=True)
    period4_bills = models.IntegerField(_("Period 4 Bill"),default=0, null=True)
    period5_bills = models.IntegerField(_("Period 5 Bill"),default=0, null=True)
    period6_bills = models.IntegerField(_("Period 6 Bill"),default=0, null=True)

    def __str__(self):
        return str(self.caterer.name)

    class Meta:
        verbose_name = "Caterer Bill"
        verbose_name_plural = "Caterer Bills"
