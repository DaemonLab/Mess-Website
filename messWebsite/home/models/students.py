from django.db import models
from django.utils.translation import gettext as _
import datetime

kanaka=900
ajay=900
gauri=500

class Student(models.Model):
    #Student details table
#    student_id = models.ForeignKey(Allocation, default=0,on_delete=models.SET_NULL,null=True)
    name = models.CharField(_("Name of Student"), max_length=30,help_text="This contains the name of the Student")
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
#    roll_no = models.BigAutoField(primary_key=True,default=None)
    student_id =models.CharField(_("Allocation Id"), default=None,max_length=30,help_text="This contains the Allocation Id",null=True, blank=True)
    month = models.CharField(_("Month"),max_length=10,help_text="This contains for which month the allocation id is alloted")
    caterer_name = models.CharField(_("Caterer Name"), max_length=50, help_text="The text in this text field contains the caterer name.")
    high_tea = models.BooleanField(_("High Tea"),help_text="This contains the info if high tea is taken or not")
    first_pref = models.CharField(_("First Preference"),default=None, max_length=10, help_text="This contians the first preference caterer of the student")
    second_pref = models.CharField(_("Second Preference"),default=None, max_length=10, help_text="This contians the first preference caterer of the student")
    third_pref = models.CharField(_("Third Preference"),default=None, max_length=10, help_text="This contians the first preference caterer of the student")
    
    def save(self,*args,**kwargs):
#        self.roll_no=self.student_data.roll_no
        global kanaka, gauri, ajay
        # print(kanaka)
        for pref in {self.first_pref,self.second_pref,self.third_pref}:
#            print(pref)
            if(pref == "kanaka" and kanaka>0):
                self.student_id="K"+str(kanaka)
                self.caterer_name = "Kanaka"
                # print("hi")
                kanaka-=1
                break 
                super().save(*args,**kwargs)
            elif(pref == "ajay" and ajay>0):
                self.student_id="A"+str(ajay)
                self.caterer_name = "Ajay"
                # print("hi2")
                ajay-=1
                break
                super().save(*args,**kwargs)
            elif(pref == "gauri" and gauri>0):
                self.student_id="G"+str(gauri)
                self.caterer_name = "Gauri"
                # print("hi0")
                gauri-=1
                break
                super().save(*args,**kwargs)
        super().save(*args,**kwargs)


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
    allocation_id = models.ForeignKey(Allocation, default=0,on_delete=models.SET_NULL,null=True)
    start_date = models.DateField(help_text="start date of the rebate")
    end_date = models.DateField(help_text="end date of the rebate")
#    print(str(start_date))
    approved = models.BooleanField(default=False,help_text="tells if the rebate is approved")

    def save(self,*args,**kwargs):
        diff = abs((self.end_date-self.start_date).days)
        diff2 = (self.start_date-datetime.date.today()).days
        print(self.approved)
        print(diff2)
        if((diff)<=7 and diff2>=2):
            self.approved = True
        else:
            self.approved = False
        super().save(*args,**kwargs)
    
    
    def __str__(self):
#        return self.start_date
        return "Rebate of " + self.allocation_id.student_id
    
    class Meta:
        verbose_name = "Rebate Details"
        verbose_name_plural = "Rebate Details"
