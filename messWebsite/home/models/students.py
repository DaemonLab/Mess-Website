from django.db import models
from django.utils.translation import gettext as _

class Allocation(models.Model):
    #Allocation details
    allocation_id =models.CharField(_("Allocation Id"), max_length=30,help_text="This contains the Allocation Id")
    month = models.CharField(_("Month"),max_length=10,help_text="This contains for which month the allocation id is alloted")
    caterer_name = models.CharField(_("Caterer Name"), max_length=50, help_text="The text in this text field contains the caterer name.")
    high_tea = models.BooleanField(_("High Tea"),help_text="This contains the info if high tea is taken or not")

    def __str__(self):
        return "Allocation id : " + self.allocation_id
    
    class Meta:
        verbose_name = "Allocation Details"
        verbose_name_plural = "Allocation Details"

class Student(models.Model):
    #Student details table
    name = models.CharField(_("Name of Student"), max_length=30,help_text="This contains the name of the Student")
    roll_no = models.CharField(_("Roll number of Student"), max_length=10,help_text="This contains the roll number of the Student")
    department = models.CharField(_("Department of Student"), max_length=30,help_text="This contains the department of the Student")
    degree = models.CharField(_("Degree of Student"), max_length=10,help_text="This contains the degree of the Student")
    hostel = models.CharField(_("Hostel of Student"), max_length=3,help_text="This contains the hostel of the Student")
    room_no = models.CharField(_("Room Number of Student"), max_length=5,help_text="This contains the room number of the Student")
    allocation_id = models.ForeignKey(Allocation, default=0,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return "Student :" + str(self.roll_no)
    
    class Meta:
        verbose_name = "Student Details"
        verbose_name_plural = "Student Details"


class Scan(models.Model):
    #Scan details of each allocation id
    allocation_id = models.ForeignKey(Allocation, default=0,on_delete=models.SET_NULL,null=True)
    date = models.DateField(help_text="Date of the scan details")
    breakfast = models.BooleanField(_("Breakfast"),help_text="This contains if the breeakfast was eaten by the student")
    lunch = models.BooleanField(_("lunch"),help_text="This contains if the lunch was eaten by the student")
    high_tea = models.BooleanField(_("high_tea"),help_text="This contains if the high tea was eaten by the student")
    dinner = models.BooleanField(_("dinner"),help_text="This contains if the dinner was eaten by the student")

    def __str__(self):
        return "Scan Details of " + self.allocation_id.allocation_id
    
    class Meta:
        verbose_name = "Scan Details"
        verbose_name_plural = "Scan Details"

class Rebate(models.Model):
    allocation_id = models.ForeignKey(Allocation, default=0,on_delete=models.SET_NULL,null=True)
    start_date = models.DateField(help_text="start date of the rebate")
    end_date = models.DateField(help_text="end date of the rebate")

    def __str__(self):
        return "Rebate of " + self.allocation_id.allocation_id
    
    class Meta:
        verbose_name = "Rebate Details"
        verbose_name_plural = "Rebate Details"