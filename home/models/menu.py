from django.db import models
from django.utils.translation import gettext as _

class Menu(models.Model):
    """
    Stores different types of menus with their respective Google Sheets URLs.
    Ensures that only one object exists for each menu type.
    """
    GENERAL = "General"
    SICK_FOOD = "Sick Food"
    JAIN = "Jain"
    
    MENU_CHOICES = [
        (GENERAL, "General Menu"),
        (SICK_FOOD, "Sick Food Menu"),
        (JAIN, "Jain Menu"),
    ]
    
    menu_type = models.CharField(
        _("Menu Type"),
        max_length=20,
        choices=MENU_CHOICES,
        unique=True,
        help_text="The type of menu (General, Sick Food, Jain). Only one instance per type is allowed."
    )
    sheet_url = models.URLField(
        _("Menu URL"),
        help_text="The Google Sheets URL containing the respective menu.",
    )
    
    def __str__(self):
        return f"{self.menu_type} Menu"
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
