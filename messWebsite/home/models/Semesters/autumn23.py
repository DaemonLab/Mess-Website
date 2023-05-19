from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
from ..students import Student
from ..caterer import Caterer
class PeriodAutumn23(models.Model):
    Sno = models.IntegerField(_("Sno"),default=0,help_text="This contains the serial number of the Period")
    period = models.CharField(max_length=30,help_text="This contains the period of the allotement of this semester",default="",null=True,blank=True)

    def __str__(self):
        return "Period :" + str(self.period) + str(self.Sno)

    class Meta:
        verbose_name = "Period Details for Autumn 2023"
        verbose_name_plural = "Period Details for Autumn 2023"


class AllocationAutumn23(models.Model):
    """
    Stores the Allocation details
    """

    roll_no = models.ForeignKey(
        Student, default=0, on_delete=models.SET_NULL, null=True
    )
    student_id = models.CharField(
        _("Allocation Id"),
        default=None,
        max_length=30,
        help_text="This contains the Allocation Id",
        null=True,
        blank=True,
    )
    month = models.ForeignKey(
        PeriodAutumn23, default=0, on_delete=models.SET_NULL, null=True
    )
    caterer_name = models.CharField(
        _("Caterer Name"),
        max_length=50,
        help_text="The text in this text field contains the caterer name.",
        default="",null=True,blank=True
    )
    high_tea = models.BooleanField(
        _("High Tea"), help_text="This contains the info if high tea is taken or not",
        default=False,null=True,blank=True
    )
    first_pref = models.CharField(
        _("First Preference"),
        default=None,
        max_length=10,
        help_text="This contians the first preference caterer of the student",
        null=True,blank=True
    )
    second_pref = models.CharField(
        _("Second Preference"),
        default=None,
        max_length=10,
        help_text="This contians the first preference caterer of the student",
        null=True,blank=True
    )
    third_pref = models.CharField(
        _("Third Preference"),
        default=None,
        max_length=10,
        help_text="This contians the first preference caterer of the student",
        null=True,blank=True
    )

    def __str__(self):
        return self.student_id

    class Meta:
        verbose_name = "Allocation Details for Autumn 2023"
        verbose_name_plural = "Allocation Details for Autumn 2023"


class RebateAutumn23(models.Model):
    """
    Storing the Rebate Bills of the Students for the Autumn Semester
    """
    email = models.ForeignKey(Student, on_delete=models.SET_NULL, default="", null=True)

    julyShort = models.IntegerField(_("July Short"),default=0, null=True)
    julyLong = models.IntegerField(_("July Long"),default=0,null=True)
    highTeaJuly = models.BooleanField(_("July High Tea"),default=True)
    julyBill = models.IntegerField(_("July Rebate Amount"),default=0, null=True)

    augustShort = models.IntegerField(_("August Short"),default=0, null=True)
    augustLong = models.IntegerField(_("August Long"),default=0,null=True)
    highTeaAugust = models.BooleanField(_("August High Tea"),default=True)
    augustBill = models.IntegerField(_("August Rebate Amount"),default=0, null=True)

    septemberShort = models.IntegerField(_("September Short"),default=0, null=True)
    septemberLong = models.IntegerField(_("September Long"),default=0,null=True)
    highTeaSeptember = models.BooleanField(_("September High Tea"),default=True)
    septemberBill = models.IntegerField(_("September Rebate Amount"),default=0, null=True)

    octoberShort = models.IntegerField(_("October Short"),default=0, null=True)
    octoberLong = models.IntegerField(_("October Long"),default=0,null=True)
    highTeaOctober = models.BooleanField(_("October High Tea"),default=True)
    octoberBill = models.IntegerField(_("October Rebate Amount"),default=0, null=True)

    novemberShort = models.IntegerField(_("November Short"),default=0, null=True)
    novemberLong = models.IntegerField(_("November Long"),default=0,null=True)
    highTeaNovember = models.BooleanField(_("November High Tea"),default=True)
    NovemberBill = models.IntegerField(_("November Rebate Amount"),default=0, null=True)

    decemberShort = models.IntegerField(_("December Short"),default=0, null=True)
    decemberLong = models.IntegerField(_("December Long"),default=0,null=True)
    highTeaDecember = models.BooleanField(_("December High Tea"),default=True)
    decemberBill = models.IntegerField(_("December Rebate Amount"),default=0, null=True)

    def __str__(self):
        return str(self.email.email)

    class Meta:
        verbose_name = "Rebate Bill Autumn 2023"
        verbose_name_plural = "Rebate Bills Autumn 2023"

class CatererBillsAutumn23(models.Model):
    """
    Storing the Bills of the Caterers for the Autumn Semester
    """
    Caterer = models.ForeignKey(Caterer,max_length=30, default="",on_delete=models.SET_NULL, null=True)

    julyBill = models.IntegerField(_("July Bill"),default=0, null=True)
    augustBill = models.IntegerField(_("August Bill"),default=0, null=True)
    septemberBill = models.IntegerField(_("September Bill"),default=0, null=True)
    octoberBill = models.IntegerField(_("October Bill"),default=0, null=True)
    novemberBill = models.IntegerField(_("November Bill"),default=0, null=True)
    decemberBill = models.IntegerField(_("December Bill"),default=0, null=True)

    def __str__(self):
        return str(self.Caterer.name)

    class Meta:
        verbose_name = "Caterer Bill Autumn 2023"
        verbose_name_plural = "Caterer Bills Autumn 2023"
