from django.db import models
from django.utils.translation import gettext as _



class RebateAutumnSem(models.Model):
    """
    Storing the Rebate Bills of the Students for the Autumn Semester
    """
    email = models.CharField(max_length=30, default="", null=True)

    julyShort = models.IntegerField(default=0, null=True)
    julyLong = models.IntegerField(default=0,null=True)
    highTeaJuly = models.BooleanField(default=True)
    julyBill = models.IntegerField(default=0, null=True)

    augustShort = models.IntegerField(default=0, null=True)
    augustLong = models.IntegerField(default=0,null=True)
    highTeaAugust = models.BooleanField(default=True)
    augustBill = models.IntegerField(default=0, null=True)

    septemberShort = models.IntegerField(default=0, null=True)
    septemberLong = models.IntegerField(default=0,null=True)
    highTeaSeptember = models.BooleanField(default=True)
    septemberBill = models.IntegerField(default=0, null=True)

    octoberShort = models.IntegerField(default=0, null=True)
    octoberLong = models.IntegerField(default=0,null=True)
    highTeaOctober = models.BooleanField(default=True)
    octoberBill = models.IntegerField(default=0, null=True)

    novemberShort = models.IntegerField(default=0, null=True)
    novemberLong = models.IntegerField(default=0,null=True)
    highTeaNovember = models.BooleanField(default=True)
    NovemberBill = models.IntegerField(default=0, null=True)

    decemberShort = models.IntegerField(default=0, null=True)
    decemberLong = models.IntegerField(default=0,null=True)
    highTeaDecember = models.BooleanField(default=True)
    decemberBill = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Rebate Bill Autumn Semester"
        verbose_name_plural = "Rebate Bills Autumn Semester"


class RebateSpringSem(models.Model):
    """
    Storing the Rebate Bills of the Students for the Spring Semester
    """
    email = models.CharField(max_length=30, default="", null=True)

    januaryShort = models.IntegerField(default=0, null=True)
    januaryLong = models.IntegerField(default=0,null=True)
    highTeaJanuary = models.BooleanField(default=True)
    januaryBill = models.IntegerField(default=0,null=True)

    feburaryShort = models.IntegerField(default=0, null=True)
    feburaryLong = models.IntegerField(default=0,null=True)
    highTeaFeburary = models.BooleanField(default=True)
    feburaryBill = models.IntegerField(default=0,null=True)

    marchShort = models.IntegerField(default=0, null=True)
    marchLong = models.IntegerField(default=0,null=True)
    highTeaMarch = models.BooleanField(default=True)
    marchBill = models.IntegerField(default=0,null=True)

    aprilShort = models.IntegerField(default=0, null=True)
    aprilLong = models.IntegerField(default=0,null=True)
    highTeaApril = models.BooleanField(default=True)
    aprilBill = models.IntegerField(default=0,null=True)

    mayShort = models.IntegerField(default=0, null=True)
    mayLong = models.IntegerField(default=0,null=True)
    highTeaMay = models.BooleanField(default=True)
    mayBill = models.IntegerField(default=0,null=True)

    juneShort = models.IntegerField(default=0, null=True)
    juneLong = models.IntegerField(default=0,null=True)
    highTeaJune = models.BooleanField(default=True)
    juneBill = models.IntegerField(default=0,null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Rebate Bill Spring Semester"
        verbose_name_plural = "Rebate Bills Spring Semester"