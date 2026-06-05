import uuid
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from .students import Student
from qrscan.models import MessCard


class SpecialEvent(models.Model):
    """
    Stores Special Event Details
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="This contains the unique id of the special event"
    )
    name = models.CharField(
        max_length=100,
        help_text="This contains the name of the special event"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="This contains the description of the special event"
    )
    event_date = models.DateTimeField(
        help_text="This contains the date and time of the special event"
    )
    location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="This contains the location of the special event"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        help_text="This contains the status of the special event"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        help_text="This contains the user who created the event"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="This contains the creation time of the event"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="This contains the last update time of the event"
    )

    class Meta:
        verbose_name = "Special Event"
        verbose_name_plural = "Special Events"
        ordering = ['-event_date']

    def __str__(self):
        return f"{self.name} - {self.event_date.strftime('%Y-%m-%d %H:%M')}"


class EventInvitation(models.Model):
    """
    Stores Event Invitation Details
    """
    INVITATION_STATUS_CHOICES = [
        ('invited', 'Invited'),
        ('attended', 'Attended'),
        ('absent', 'Absent'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="This contains the unique id of the invitation"
    )
    event = models.ForeignKey(
        SpecialEvent,
        on_delete=models.CASCADE,
        related_name='invitations',
        help_text="This contains the special event"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='event_invitations',
        help_text="This contains the student details"
    )
    email = models.CharField(
        max_length=100,
        help_text="This contains the email of the student"
    )
    status = models.CharField(
        max_length=20,
        choices=INVITATION_STATUS_CHOICES,
        default='invited',
        help_text="This contains the invitation status"
    )
    invited_at = models.DateTimeField(
        auto_now_add=True,
        help_text="This contains the invitation time"
    )
    attended_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="This contains the attendance time"
    )

    class Meta:
        verbose_name = "Event Invitation"
        verbose_name_plural = "Event Invitations"
        unique_together = ('event', 'student')
        ordering = ['-invited_at']

    def __str__(self):
        return f"{self.student.email} - {self.event.name}"


class EventScan(models.Model):
    """
    Stores Event QR Code Scan Details
    """
    SCAN_STATUS_CHOICES = [
        ('success', 'Success'),
        ('not_invited', 'Not Invited'),
        ('already_scanned', 'Already Scanned'),
        ('failed', 'Failed'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="This contains the unique id of the scan"
    )
    event = models.ForeignKey(
        SpecialEvent,
        on_delete=models.CASCADE,
        related_name='scans',
        help_text="This contains the special event"
    )
    mess_card = models.ForeignKey(
        MessCard,
        on_delete=models.CASCADE,
        help_text="This contains the mess card details"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        help_text="This contains the student details"
    )
    verification_status = models.CharField(
        max_length=20,
        choices=SCAN_STATUS_CHOICES,
        help_text="This contains the scan verification status"
    )
    scanned_at = models.DateTimeField(
        auto_now_add=True,
        help_text="This contains the scan time"
    )

    class Meta:
        verbose_name = "Event Scan"
        verbose_name_plural = "Event Scans"
        ordering = ['-scanned_at']

    def __str__(self):
        return f"{self.event.name} - {self.student.email} - {self.verification_status}"
