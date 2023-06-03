from django.db import models
from django.utils.translation import gettext as _


class About(models.Model):
    """
    Stores Single About on Home Page
    """
    description = models.TextField(_("Description"), 
                                   help_text="The text added in this text field will show up in the about section of the home page.")

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
    update = models.CharField(_("update"), max_length=120,
                              help_text="The text added in this text field will show as one of the update in the update section")
    time_stamp = models.DateTimeField(auto_now_add=True, 
                                      help_text="time stamp of the update will also show up on the page and this also decides the order of the updates that show up")

    def __str__(self):
        return "Posted on " + self.time_stamp.strftime("%m/%d/%Y, %H:%M:%S")

    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"


# class Photos(models.Model):
#     """
#     Stores All phtographs on the bottom of the Home page
#     """
#     image = models.ImageField(_("Photographs on Home page"), upload_to="static/images")
#     poc = models.CharField(_("Point of Contact"), max_length=30, default='',
#                            help_text="This contains the name of the person in the photograph")
#     occupation = models.CharField(_("Occupation"), max_length=50, default='',
#                                   help_text="This contains the occupation of the person in the photograph")

#     def __str__(self):
#         return "Home Page Photographs"

#     class Meta:
#         verbose_name = " General Photographs"
#         verbose_name_plural = " General Photographs"
