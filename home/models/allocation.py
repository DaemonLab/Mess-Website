from django.db import models
from django.utils.translation import gettext as _

from .caterer import Caterer


class Semester(models.Model):
    name = models.CharField(_("Semester Name"), max_length=30, default=None, null=True, blank=True, help_text="Name of the semester")

    def __str__(self):
        return self.name
    
    class meta:
        verbose_name = "Semester Details"
        verbose_name_plural="Semester Details"

class Period(models.Model):
    semester = models.ForeignKey("home.Semester", verbose_name=_("Semester"), on_delete=models.CASCADE, default=None,null=True)
    Sno = models.IntegerField(_("Sno"),default=0,help_text="This contains the serial number of the Period")
    start_date = models.DateField(help_text="This contains the start date of this Period for this semester",null=True,blank=True)
    end_date = models.DateField(help_text="This contains the end date of this Period of this semester",null=True,blank=True)

    def __str__(self):
        return str(self.Sno) + " " + str(self.semester.name)

    class Meta:
        verbose_name = "Period Details"
        verbose_name_plural = "Period Details"

class Allocation(models.Model):
    """
    Stores the Allocation details
    """
    from .students import Student
    email = models.ForeignKey(
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
    period = models.ForeignKey(
        Period, default=None, on_delete=models.SET_NULL, null=True,
        help_text="Contains the period of allocation"
    )
    caterer = models.ForeignKey(
        Caterer, default=None, on_delete=models.SET_NULL, null=True,
        help_text="Contains the allocated caterer of the student"        
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
        verbose_name = "Allocation Detail"
        verbose_name_plural = "Allocation Details"
