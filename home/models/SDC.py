from django.db import models
from django.utils.translation import gettext as _
from home.models import Student

class SDC(models.Model):
    """
    Stores details of SDC members, linked to the Student table.
    """
    POSITION_CHOICES = [
        ("Head", "Head"),
        ("Advisory", "Advisory"),
        ("Member", "Member"),
    ]

    YEAR_CHOICES = [
        (2024, "2024"),
        (2025, "2025"),
    ]

    student = models.OneToOneField(
        Student, 
        on_delete=models.CASCADE, 
        related_name="sdc_profile",
        help_text="Reference to the Student table"
    )
    name = models.CharField(
        _("Name of Student"),
        max_length=50,
        help_text="This contains the name of the Student in SDC",
    )
    image = models.ImageField(
        upload_to="sdc_images/", 
        blank=True, 
        null=True,
        help_text="Profile image of the Student in SDC"
    )
    position = models.CharField(
        _("Position in SDC"),
        max_length=20,
        choices=POSITION_CHOICES,
        help_text="This contains the position of the Student in SDC"
    )
    year = models.IntegerField(
        _("Year"),
        choices=YEAR_CHOICES,
        help_text="Select the year for SDC membership"
    )

    def __str__(self):
        return f"{self.name} - {self.position} ({self.year})"

    class Meta:
        verbose_name = "SDC Member"
        verbose_name_plural = "SDC Members"
