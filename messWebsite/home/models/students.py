from django.db import models
from django.utils.translation import gettext as _
import datetime
from django.utils.timezone import now

class Student(models.Model):
    #Student details table
    name = models.CharField(_("Name of Student"), max_length=30,help_text="This contains the name of the Student")
    email = models.CharField(max_length=30, default="")
    roll_no = models.CharField(_("Roll number of Student"), max_length=10,help_text="This contains the roll number of the Student")
    department = models.CharField(_("Department of Student"), max_length=30,help_text="This contains the department of the Student")
    degree = models.CharField(_("Degree of Student"), max_length=10,help_text="This contains the degree of the Student")
    hostel = models.CharField(_("Hostel of Student"), max_length=3,help_text="This contains the hostel of the Student")
    room_no = models.CharField(_("Room Number of Student"), max_length=5,help_text="This contains the room number of the Student")
    
    def __str__(self):
        return "Student :" + str(self.roll_no)
    
    class Meta:
        verbose_name = "Student Details"
        verbose_name_plural = "Student Details"

class Allocation(models.Model):
    #Allocation details
    roll_no = models.ForeignKey(Student,default=0,on_delete=models.SET_NULL,null=True)
    student_id =models.CharField(_("Allocation Id"), default=None,max_length=30,help_text="This contains the Allocation Id",null=True, blank=True)
    month = models.CharField(_("Month"),max_length=10,help_text="This contains for which month the allocation id is alloted")
    caterer_name = models.CharField(_("Caterer Name"), max_length=50, help_text="The text in this text field contains the caterer name.")
    high_tea = models.BooleanField(_("High Tea"),help_text="This contains the info if high tea is taken or not")
    first_pref = models.CharField(_("First Preference"),default=None, max_length=10, help_text="This contians the first preference caterer of the student")
    second_pref = models.CharField(_("Second Preference"),default=None, max_length=10, help_text="This contians the first preference caterer of the student")
    third_pref = models.CharField(_("Third Preference"),default=None, max_length=10, help_text="This contians the first preference caterer of the student")

    def __str__(self):
        return "Allocation id : " + self.student_id
    
    class Meta:
        verbose_name = "Allocation Details"
        verbose_name_plural = "Allocation Details"

class Scan(models.Model):
    #Scan details of each allocation id
    student_id = models.ForeignKey(Allocation, default=0,on_delete=models.SET_NULL,null=True)
    date = models.DateField(help_text="Date of the scan details")
    breakfast = models.BooleanField(_("Breakfast"),help_text="This contains if the breeakfast was eaten by the student")
    lunch = models.BooleanField(_("lunch"),help_text="This contains if the lunch was eaten by the student")
    high_tea = models.BooleanField(_("high_tea"),help_text="This contains if the high tea was eaten by the student")
    dinner = models.BooleanField(_("dinner"),help_text="This contains if the dinner was eaten by the student")

    def __str__(self):
        return "Scan Details of " + self.student_id.student_id
    
    class Meta:
        verbose_name = "Scan Details"
        verbose_name_plural = "Scan Details"

class Rebate(models.Model):
    email = models.CharField(max_length=30, default=0)
    allocation_id = models.ForeignKey(Allocation, related_name="allocation_id", default=0,on_delete=models.SET_NULL,null=True)
    start_date = models.DateField(help_text="start date of the rebate")
    end_date = models.DateField(help_text="end date of the rebate")
    approved = models.BooleanField(default=False,help_text="tells if the rebate is approved")
    date_applied = models.DateField(default=now,help_text="Date on which the rebate was applied")

    def __str__(self):
        return str(self.allocation_id) + " " + str(self.date_applied)
    
    class Meta:
        verbose_name = "Rebate Details"
        verbose_name_plural = "Rebate Details"

class File(models.Model):
    file = models.FileField(upload_to="static/")

class RebateAutumnSem(models.Model):
    email = models.CharField(max_length=30, default="", null=True)
    july = models.IntegerField(default=0,null=True)
    highTeaJuly = models.BooleanField(default=True)
    august = models.IntegerField(default=0,null=True)
    highTeaAugust = models.BooleanField(default=True)
    september = models.IntegerField(default=0,null=True)
    highTeaSeptember = models.BooleanField(default=True)
    october = models.IntegerField(default=0,null=True)
    highTeaOctober = models.BooleanField(default=True)
    november = models.IntegerField(default=0,null=True)
    highTeaNovember = models.BooleanField(default=True)
    december = models.IntegerField(default=0,null=True)
    highTeaDecember = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name = "Rebate Bill Autumn Semester"
        verbose_name_plural = "Rebate Bills Autumn Semester"

class RebateSpringSem(models.Model):
    email = models.CharField(max_length=30, default="", null=True)
    january = models.IntegerField(default=0,null=True)
    highTeaJanuary = models.BooleanField(default=True)
    feburary = models.IntegerField(default=0,null=True)
    highTeaFeburary = models.BooleanField(default=True)
    march = models.IntegerField(default=0,null=True)
    highTeaMarch = models.BooleanField(default=True)
    april = models.IntegerField(default=0,null=True)
    highTeaApril = models.BooleanField(default=True)
    may = models.IntegerField(default=0,null=True)
    highTeaMay = models.BooleanField(default=True)
    june = models.IntegerField(default=0,null=True)
    highTeaJune = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name = "Rebate Bill Spring Semester"
        verbose_name_plural = "Rebate Bills Spring Semester"