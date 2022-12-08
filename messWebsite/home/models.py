from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

#will only show one value
class About(models.Model): 
    description = models.TextField(_("Description"))

    def __str__(self):
        return "About Us Content"

#will show all updates, using for loop
class Update(models.Model):
    update = models.CharField(_("update"),max_length=120)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "posted on "+ self.time_stamp

#will show all rules, using for loop
class Rule(models.Model):
    rule = models.TextField(_("Rule"))


class Penalty(models.Model):
    penalty = models.TextField(_("Penalty")) 

#will only show one value
class ShortRebate(models.Model):
    desc = models.TextField()
    link = models.URLField()
    policy = models.TextField()
    circulation = models.TextField()
    infoToCaterer = models.TextField()
    note = models.TextField()
    Memebers = models.TextField()
    biling = models.TextField()

#will show all point of long term rebate, using for loop
class LongRebate(models.Model):
    rule= models.TextField()

class Caterer(models.Model):
    name=models.CharField(_("Caterer Name"), max_length=50)
    upper_description = models.TextField(_("Upper Description"))
    sheet_url = models.URLField(_("Menu URL"))
    lower_description = models.TextField(_("Lower Discription"))

    def __str__(self):
        return "Caterer "+ self.name

#will show all links, using for loop
class Form(models.Model):
    heading = models.CharField(_("From Heading"),max_length=30)
    description = models.CharField(_("Form Description"),max_length=120)
    url = models.URLField(_("Form URL"))

    def __str__(self):
        return "Form "+ self.heading

#will show all cafeterias, using for loop
class Cafeteria(models.Model):
#   sno = models.AutoField(primary_key=True)
    name = models.CharField(_("Name of Cafeteria"),max_length=30)
    poc = models.CharField(_("Point of Contact"),max_length=30)
    contact = models.CharField(_("Phone Number"),max_length=10, null=True,blank=True)

    def __str__(self):
        return "Cafeteria "+ self.name

#will show all contact, using for loop and checking each position using heading tag
class Contact(models.Model):
    occupation = models.CharField(_("Occupation"),max_length=5)
    hostel_sec = models.BooleanField(_("Dining Secretary"))
    name = models.CharField(_("Name"),max_length=30,null=True,blank=True)
    contact = models.CharField(_("Phone Number"),max_length=10, null=True,blank=True)
    email = models.EmailField(_("Email"))

    def __str__(self):
        return "Contact of "+ self.occupation + "Dining Secretary - "+ self.hostel_sec
