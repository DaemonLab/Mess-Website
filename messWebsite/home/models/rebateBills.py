from django.db import models
from django.utils.translation import gettext as _
from .students import Student

class RebateAutumnSem(models.Model):
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
        return str(self.email)

    class Meta:
        verbose_name = "Rebate Bill Autumn Semester"
        verbose_name_plural = "Rebate Bills Autumn Semester"


class RebateSpringSem(models.Model):
    """
    Storing the Rebate Bills of the Students for the Spring Semester
    """
    email = models.ForeignKey(Student, on_delete=models.SET_NULL, default="", null=True)

    januaryShort = models.IntegerField(_("January Short"),default=0, null=True)
    januaryLong = models.IntegerField(_("January Long"),default=0,null=True)
    highTeaJanuary = models.BooleanField(_("January High Tea"),default=True)
    januaryBill = models.IntegerField(_("January Rebate Amount"),default=0,null=True)

    feburaryShort = models.IntegerField(_("Feburary Short"),default=0, null=True)
    feburaryLong = models.IntegerField(_("Feburary Long"),default=0,null=True)
    highTeaFeburary = models.BooleanField(_("Feburary High Tea"),default=True)
    feburaryBill = models.IntegerField(_("Feburary Rebate Amount"),default=0,null=True)

    marchShort = models.IntegerField(_("March Short"),default=0, null=True)
    marchLong = models.IntegerField(_("March Long"),default=0,null=True)
    highTeaMarch = models.BooleanField(_("March High Tea"),default=True)
    marchBill = models.IntegerField(_("March Rebate Amount"),default=0,null=True)

    aprilShort = models.IntegerField(_("April Short"),default=0, null=True)
    aprilLong = models.IntegerField(_("April Long"),default=0,null=True)
    highTeaApril = models.BooleanField(_("April High Tea"),default=True)
    aprilBill = models.IntegerField(_("April Rebate Amount"),default=0,null=True)

    mayShort = models.IntegerField(_("May Short"),default=0, null=True)
    mayLong = models.IntegerField(_("May Long"),default=0,null=True)
    highTeaMay = models.BooleanField(_("May High Tea"),default=True)
    mayBill = models.IntegerField(_("May Rebate Amount"),default=0,null=True)

    juneShort = models.IntegerField(_("June Short"),default=0, null=True)
    juneLong = models.IntegerField(_("June Long"),default=0,null=True)
    highTeaJune = models.BooleanField(_("June High Tea"),default=True)
    juneBill = models.IntegerField(_("June Rebate Amount"),default=0,null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Rebate Bill Spring Semester"
        verbose_name_plural = "Rebate Bills Spring Semester"

