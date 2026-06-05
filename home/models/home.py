from django.db import models
from django.utils.translation import gettext as _


class About(models.Model):
    """
    Stores Single About on Home Page
    """

    description = models.TextField(
        _("Description"),
        help_text="The text added in this text field will show up in the about section of the home page.",
    )

    def __str__(self):
        return "About Us Content"

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Carousel(models.Model):
    """
    Stores All carousel images on Home page
    """

    image = models.ImageField(_("Carousel Images"), upload_to="static/images")

    def __str__(self):
        return "Carousel Images"

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"


class Update(models.Model):
    """
    Stores All Updates on Home Page
    """

    update = models.CharField(
        _("update"),
        max_length=120,
        help_text="The text added in this text field will show as one of the update in the update section",
    )
    time_stamp = models.DateTimeField(
        auto_now_add=True,
        help_text="time stamp of the update will also show up on the page and this also decides the order of the updates that show up",
    )

    def __str__(self):
        return "Posted on " + self.time_stamp.strftime("%m/%d/%Y, %H:%M:%S")

    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"


class GlobalConstants(models.Model):
    """
    Stores globally accessible constants for the website like rebate limits.
    """

    short_rebate_stretch_limit = models.IntegerField(
        _("Short Rebate Stretch Limit"),
        default=10,
        help_text="Maximum number of days for a single short rebate application.",
    )
    short_rebate_period_limit = models.IntegerField(
        _("Short Rebate Period Limit"),
        default=10,
        help_text="Maximum total days allowed for short rebates within a single period.",
    )
    min_rebate_days = models.IntegerField(
        _("Minimum Rebate Days"),
        default=2,
        help_text="Minimum number of days required for a rebate application.",
    )
    days_prior_notice = models.IntegerField(
        _("Days Prior Notice"),
        default=2,
        help_text="Minimum days before leave commencement the form must be filled.",
    )

    def __str__(self):
        return "Global Constants"

    class Meta:
        verbose_name = "Global Constant"
        verbose_name_plural = "Global Constants"
