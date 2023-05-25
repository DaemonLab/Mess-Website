from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
import datetime

class Student(models.Model):
    """
    Stores Student Details
    """

    name = models.CharField(
        _("Name of Student"),
        max_length=30,
        help_text="This contains the name of the Student",
    )
    email = models.CharField(max_length=30, default="")
    roll_no = models.CharField(
        _("Roll number of Student"),
        max_length=10,
        help_text="This contains the roll number of the Student",
    )
    department = models.CharField(
        _("Department of Student"),
        max_length=30,
        help_text="This contains the department of the Student",
        null=True,
    )
    degree = models.CharField(
        _("Academic Program"),
        max_length=10,
        help_text="This contains the degree of the Student",
    )
    hostel = models.CharField(
        _("Hostel of Student"),
        max_length=3,
        help_text="This contains the hostel of the Student",
    )
    room_no = models.CharField(
        _("Room Number of Student"),
        max_length=5,
        help_text="This contains the room number of the Student",
    )

    def __str__(self):
        return "Student :" + str(self.roll_no)

    class Meta:
        verbose_name = "Student Details"
        verbose_name_plural = "Student Details"


class Allocation(models.Model):
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
    month = models.CharField(
        _("Month"),
        max_length=10,
        help_text="This contains for which month the allocation id is alloted",
        default="",null=True,blank=True
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
        verbose_name = "Allocation Details"
        verbose_name_plural = "Allocation Details"


class Scan(models.Model):
    """ "
    Stores the Scan details of each allocation id
    Note: this is not implemented yet
    """

    student_id = models.ForeignKey(
        Allocation, default=0, on_delete=models.SET_NULL, null=True
    )
    date = models.DateField(help_text="Date of the scan details")
    breakfast = models.BooleanField(
        _("Breakfast"),
        help_text="This contains if the breeakfast was eaten by the student",
    )
    lunch = models.BooleanField(
        _("lunch"), help_text="This contains if the lunch was eaten by the student"
    )
    high_tea = models.BooleanField(
        _("high_tea"),
        help_text="This contains if the high tea was eaten by the student",
    )
    dinner = models.BooleanField(
        _("dinner"), help_text="This contains if the dinner was eaten by the student"
    )

    def __str__(self):
        return "Scan Details of " + self.student_id.student_id

    class Meta:
        verbose_name = "Scan Details"
        verbose_name_plural = "Scan Details"


class Rebate(models.Model):
    """
    Stores the rebate details of every student
    """

    email = models.CharField(max_length=30, default=0)
    allocation_id = models.ForeignKey(
        Allocation,
        related_name="allocation_id",
        default=0,
        on_delete=models.SET_NULL,
        null=True,
    )
    start_date = models.DateField(help_text="start date of the rebate")
    end_date = models.DateField(help_text="end date of the rebate")
    approved = models.BooleanField(
        default=False, help_text="tells if the rebate is approved"
    )
    date_applied = models.DateField(
        default=now, help_text="Date on which the rebate was applied"
    )

    def __str__(self):
        return str(self.allocation_id) + " " + str(self.date_applied)

    class Meta:
        verbose_name = "Rebate Details"
        verbose_name_plural = "Rebate Details"


class LongRebate(models.Model):
    """
    Stores the long rebate details of every student
    """

    email = models.CharField(_("email"), max_length=30, default="")
    # allocation_id_id = models.ForeignKey(
    #     Allocation,
    #     related_name="allocation_id_long",
    #     default=0,
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    start_date = models.DateField(help_text="start date of the rebate",null=True, blank=True)
    end_date = models.DateField(help_text="end date of the rebate",null=True, blank=True)   
    days = models.IntegerField(_("days"), default=0)
    approved = models.BooleanField(_("Approved"), default=False)
    date_applied = models.DateField(
        default=now, help_text="Date on which the rebate was applied"
    )
    file = models.FileField(
        _("File"), upload_to="documents/", default=None, null=True, blank=True
    )

    def __str__(self):
        return str(self.date_applied)

    class Meta:
        verbose_name = "Long Rebate Details"
        verbose_name_plural = "Long Rebate Details"

class UnregisteredStudent(models.Model):
    """
    Stores the long rebate details of every student
    """
    from .Semesters.spring23 import PeriodSpring23
    from .Semesters.autumn23 import PeriodAutumn23
    from .Semesters.autumn22 import PeriodAutumn22
    email = models.CharField(_("email"), max_length=30, default="")
    period = models.ForeignKey(PeriodSpring23, default=0, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Unregistered Students"
        verbose_name_plural = "Unregistered Students"

class TodayRebate(models.Model):
    date = models.DateField(help_text="Date of the rebate",default=now)
    Caterer = models.CharField(max_length=30, default="")
    allocation_id = models.CharField(max_length=30, default="")
    start_date = models.DateField(help_text="start date of the rebate",null=True, blank=True)
    end_date = models.DateField(help_text="end date of the rebate",null=True, blank=True)

    def __str__(self):
        return str(self.date)
    
    class Meta:
        verbose_name = "Today's Rebate"
        verbose_name_plural = "Today's Rebate"

class LeftLongRebate(models.Model):
    email = models.CharField(_("email"), max_length=30, default="")
    start_date = models.DateField(help_text="start date of the rebate",null=True, blank=True)
    end_date = models.DateField(help_text="end date of the rebate",null=True, blank=True)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name = "Left Long Rebate"
        verbose_name_plural = "Left Long Rebate"