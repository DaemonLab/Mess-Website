from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Student(models.Model):
    """
    Stores Student Details
    """

    name = models.CharField(
        _("Name of Student"),
        max_length=50,
        help_text="This contains the name of the Student",
        null=True,
        default="",
        blank=True,
    )
    email = models.CharField(max_length=50, default="")
    roll_no = models.CharField(
        _("Roll number of Student"),
        max_length=10,
        help_text="This contains the roll number of the Student",
        null=True,
        default="",
        blank=True,
    )
    department = models.CharField(
        _("Department of Student"),
        max_length=50,
        help_text="This contains the department of the Student",
        null=True,
        default="",
        blank=True,
    )
    degree = models.CharField(
        _("Academic Program"),
        max_length=10,
        help_text="This contains the degree of the Student",
        null=True,
        default="",
        blank=True,
    )
    hostel = models.CharField(
        _("Hostel of Student"),
        max_length=3,
        help_text="This contains the hostel of the Student",
        null=True,
        default="",
        blank=True,
    )
    room_no = models.CharField(
        _("Room Number of Student"),
        max_length=5,
        help_text="This contains the room number of the Student",
        null=True,
        default="",
        blank=True,
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Student Details"
        verbose_name_plural = "Student Details"


class Scan(models.Model):
    """ "
    Stores the Scan details of each allocation id
    Note: this is not implemented yet
    """

    student_id = models.ForeignKey(
        Student, default=0, on_delete=models.SET_NULL, null=True
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


from .allocation import Allocation, Period


class Rebate(models.Model):
    """
    Stores the rebate details of every student
    """

    email = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        verbose_name="Student Email",
    )
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
        verbose_name = "Short Rebate Details"
        verbose_name_plural = "Short Rebate Details"


class LongRebate(models.Model):
    """
    Stores the long rebate details of every student
    """

    email = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(
        help_text="start date of the rebate", null=True, blank=True
    )
    end_date = models.DateField(
        help_text="end date of the rebate", null=True, blank=True
    )
    days = models.IntegerField(_("days"), default=0)
    approved = models.BooleanField(_("Approved"), default=False)

    REASON_TYPE_CHOICES = (
        ("", "Choose the reason"),
        ("Incomplete form. Please submit a new rebate application", "Incomplete form"),
        (
            "Signature of approving authority missing. Please submit a new rebate application",
            "Signature missing",
        ),
        (
            "Attached file is not the rebate form. Please submit a new rebate application with correct attachment",
            "Wrong attached document",
        ),
        (
            "There is a date mismatch between the one written in the form and the one in the attached form. Please submit a new rebate application",
            "There is a date mismatch between the one written in the form and the one in the attached form",
        ),
    )

    reason = models.TextField(choices=REASON_TYPE_CHOICES, default="", blank=True)
    date_applied = models.DateField(
        default=now, help_text="Date on which the rebate was applied"
    )

    ## To delete this field when we no longer need old rebate data
    file = models.FileField(
        _("File"), upload_to="documents/", default=None, null=True, blank=True
    )

    def __str__(self):
        return str(self.date_applied) + " " + str(self.email)

    class Meta:
        verbose_name = "Long Rebate Details"
        verbose_name_plural = "Long Rebate Details"


class UnregisteredStudent(models.Model):
    """
    Stores the long rebate details of every student
    """

    email = models.CharField(_("email"), max_length=30, default="")
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Unregistered Students"
        verbose_name_plural = "Unregistered Students"


class TodayRebate(models.Model):
    date = models.DateField(help_text="Date of the rebate", default=now)
    Caterer = models.CharField(max_length=30, default="")
    allocation_id = models.ForeignKey(
        Allocation, on_delete=models.SET_NULL, null=True, blank=True
    )
    start_date = models.DateField(
        help_text="start date of the rebate", null=True, blank=True
    )
    end_date = models.DateField(
        help_text="end date of the rebate", null=True, blank=True
    )

    def __str__(self):
        return str(self.date) + " " + str(self.allocation_id)

    class Meta:
        verbose_name = "Today's Rebate"
        verbose_name_plural = "Today's Rebate"


class LeftLongRebate(models.Model):
    email = models.CharField(_("email"), max_length=30, default="")
    start_date = models.DateField(
        help_text="start date of the rebate", null=True, blank=True
    )
    end_date = models.DateField(
        help_text="end date of the rebate", null=True, blank=True
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Left Long Rebate"
        verbose_name_plural = "Left Long Rebate"


class LeftShortRebate(models.Model):
    email = models.CharField(_("email"), max_length=30, default="")
    start_date = models.DateField(
        help_text="start date of the rebate", null=True, blank=True
    )
    end_date = models.DateField(
        help_text="end date of the rebate", null=True, blank=True
    )
    date_applied = models.DateField(
        help_text="Date on which the rebate was applied", default=now
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Left Short Rebate"
        verbose_name_plural = "Left Short Rebate"


class AllocationForm(models.Model):
    heading = models.CharField(
        _("heading"), max_length=100, default="", null=True, blank=True
    )
    description = models.TextField(_("description"), default="", null=True, blank=True)
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(_("active"), default=False, null=True, blank=True)
    start_time = models.DateTimeField(
        _("Start Time"), default=now, null=True, blank=True
    )
    end_time = models.DateTimeField(_("End Time"), null=True, blank=True)

    def __str__(self):
        return str(self.heading)

    class Meta:
        verbose_name = "Allocation Form"
        verbose_name_plural = "Allocation Form"
