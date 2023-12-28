from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    Student,
    Rebate,
    LongRebate,
    UnregisteredStudent,
    RebateSpring23,
    RebateAutumn22,
    PeriodSpring23,
    AllocationAutumn22,
    AllocationSpring23,
    CatererBillsAutumn22,
    CatererBillsSpring23,  
    Allocation,
    CatererBills,
    StudentBills,
    Period,
    Fee,
)
from .utils.rebate_checker import count

"""
File-name: resources.py
Functions: StudentResource
    AllocationResource
    RebateResource
    RebateSpringResource
    RebateAutumnResource
Resource defines how objects are mapped to their import and export representations and 
handle importing and exporting data.
"""


class StudentResource(resources.ModelResource):

    def skip_row(self, instance,original, row,import_validation_errors):
        # Skip the row if any of the required fields are null/empty
        if not instance.email or not instance.name:
            return True  # Skip the row
        return super().skip_row(instance,original, row,import_validation_errors)

    class Meta:
        model = Student
        exclude = "id"
        import_id_fields = [
            "email",
        ]
        fields = (
            "name",
            "email",
            "roll_no",
            "hostel",
            "room_no",
            "degree",
            "department",
        )


class AllocationNewResource(resources.ModelResource):
    email__roll_no = fields.Field(
        attribute="email__roll_no", column_name="Roll No."
    )
    email__email = fields.Field(attribute="email__email", column_name="Email")
    email__name = fields.Field(attribute="email__name", column_name="Name")
    email__department = fields.Field(
        attribute="email__department", column_name="Department"
    )
    email__degree = fields.Field(
        attribute="email__degree", column_name="Academic Program"
    )
    email__hostel = fields.Field(attribute="email__hostel", column_name="Hostel")
    email__room_no = fields.Field(
        attribute="email__room_no", column_name="Room No."
    )
    period = fields.Field(attribute="period", column_name="Period")
    student_id = fields.Field(attribute="student_id", column_name="Student ID")
    caterer__name = fields.Field(attribute="caterer__name", column_name="Caterer Allocated")
    # high_tea = fields.Field(attribute="high_tea", column_name="High Tea")
    jain = fields.Field(attribute="jain", column_name="Jain")
    first_pref = fields.Field(attribute="first_pref", column_name="First Preferences")
    second_pref = fields.Field(
        attribute="second_pref", column_name="Second Preferences"
    )
    third_pref = fields.Field(attribute="third_pref", column_name="Third Preferences")

    class Meta:
        model = Allocation
        exclude="id"
        import_id_fields = ["email__name","email_hostel"]
        fields = (
            "email__roll_no",
            "email__email",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "period",
            "student_id",
            "caterer__name",
            # "high_tea",
            "jain",
            "first_pref",
            "second_pref",
            "third_pref",
        )

        export_order = [
            "email__roll_no",
            "email__email",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "student_id",
            "caterer__name",
            # "high_tea",
            "jain",
            "first_pref",
            "second_pref",
            "third_pref",
        ]

class RebateResource(resources.ModelResource):
    allocation_id__student_id = fields.Field(
        attribute="allocation_id__student_id", column_name="Allocation ID"
    )
    # def get_approved_value(self, obj):
    email = fields.Field(attribute="email", column_name="Email")
    allocation_id__roll_no__name = fields.Field(
        attribute="allocation_id__roll_no__name", column_name="Name"
    )
    allocation_id__roll_no__roll_no = fields.Field(
        attribute="allocation_id__roll_no__roll_no", column_name="Roll No."
    )
    allocation_id__roll_no__department = fields.Field(
        attribute="allocation_id__roll_no__department", column_name="Department"
    )
    allocation_id__roll_no__degree = fields.Field(
        attribute="allocation_id__roll_no__degree", column_name="Degree"
    )
    allocation_id__roll_no__hostel = fields.Field(
        attribute="allocation_id__roll_no__hostel", column_name="Hostel"
    )
    allocation_id__roll_no__room_no = fields.Field(
        attribute="allocation_id__roll_no__room_no", column_name="Room No."
    )
    allocation_id__caterer_name = fields.Field(
        attribute="allocation_id__caterer_name", column_name="Caterer Alloted"
    )
    allocation_id__high_tea = fields.Field(
        attribute="allocation_id__high_tea", column_name="High Tea"
    )
    date_applied = fields.Field(attribute="date_applied", column_name="date_applied")
    start_date = fields.Field(attribute="start_date", column_name="Start Date")
    end_date = fields.Field(attribute="end_date", column_name="End Date")
    approved = fields.Field(attribute="approved", column_name="Approved")

    class Meta:
        model = Rebate
        fields = (
            "email",
            "allocation_id__roll_no__name",
            "allocation_id__roll_no__roll_no",
            "allocation_id__roll_no__department",
            "allocation_id__roll_no__degree",
            "allocation_id__roll_no__hostel",
            "allocation_id__roll_no__room_no",
            "allocation_id__high_tea",
            "allocation_id__caterer_name",
            "allocation_id__student_id",
            "date_applied",
            "start_date",
            "end_date",
            "approved",
        )
        export_order = [
            "email",
            "allocation_id__roll_no__name",
            "allocation_id__roll_no__roll_no",
            "allocation_id__roll_no__department",
            "allocation_id__roll_no__degree",
            "allocation_id__roll_no__hostel",
            "allocation_id__roll_no__room_no",
            "allocation_id__high_tea",
            "allocation_id__student_id",
            "date_applied",
            "start_date",
            "end_date",
            "approved",
        ]


class LongRebateResource(resources.ModelResource):
    email__email = fields.Field(attribute="email__email", column_name="Email")
    email__roll_no = fields.Field(attribute="email__roll_no", column_name="Roll No.")
    email__name = fields.Field(attribute="email__name", column_name="Name")
    email__department = fields.Field(attribute="email__department", column_name="Department")
    email__degree = fields.Field(attribute="email__degree", column_name="Degree")
    email__hostel = fields.Field(attribute="email__hostel", column_name="Hostel")
    email__room_no = fields.Field(attribute="email__room_no", column_name="Room No.")
    date_applied = fields.Field(attribute="date_applied", column_name="date_applied")
    days = fields.Field(attribute="days", column_name="days")
    start_date = fields.Field(attribute="start_date", column_name="Start Date")
    end_date = fields.Field(attribute="end_date", column_name="End Date")
    approved = fields.Field(attribute="approved", column_name="Approved")

    class Meta:
        model = LongRebate
        exclude = "id"
        import_id_fields = [
            "email__email",
        ]
        fields = (
            "email__email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "date_applied",
            "start_date",
            "end_date",
            "days",
            "approved",
        )
        export_order = [
            "email__email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "date_applied",
            "start_date",
            "end_date",
            "days",
            "approved",
        ]


class RebateBillsResource(resources.ModelResource):
    email__email = fields.Field(
        column_name='Email',
        attribute='email__email',
    )
    email__roll_no = fields.Field(
        attribute="email__roll_no", column_name="Roll No."
    )
    email__name = fields.Field(attribute="email__name", column_name="Name")
    email__department = fields.Field(
        attribute="email__department", column_name="Department"
    )
    email__degree = fields.Field(
        attribute="email__degree", column_name="Academic Program"
    )
    email__hostel = fields.Field(attribute="email__hostel", column_name="Hostel")
    email__room_no = fields.Field(
        attribute="email__room_no", column_name="Room No."
    )
    allocation1 = fields.Field(attribute="allocation1", column_name="Allocation for period 1")
    period1_short = fields.Field(attribute="period1_short", column_name="Short Rebate 1")
    period1_long = fields.Field(attribute="period1_long", column_name="Long Rebate 1")
    period1_high_tea = fields.Field(attribute="period1_high_tea", column_name="High Tea 1")
    period1_bill = fields.Field(attribute="period1_bill", column_name="Bill 1")
    allocation2 = fields.Field(attribute="allocation2", column_name="Allocation for period 2")
    period2_short = fields.Field(attribute="period2_short", column_name="Short Rebate 2")
    period2_long = fields.Field(attribute="period2_long", column_name="Long Rebate 2")
    period2_high_tea = fields.Field(attribute="period2_high_tea", column_name="High Tea 2")
    period2_bill = fields.Field(attribute="period2_bill", column_name="Bill 2")
    allocation3 = fields.Field(attribute="allocation3", column_name="Allocation for period 3")
    period3_short = fields.Field(attribute="period3_short", column_name="Short Rebate 3")
    period3_long = fields.Field(attribute="period3_long", column_name="Long Rebate 3")
    period3_high_tea = fields.Field(attribute="period3_high_tea", column_name="High Tea 3")
    period3_bill = fields.Field(attribute="period3_bill", column_name="Bill 3")
    allocation4 = fields.Field(attribute="allocation4", column_name="Allocation for period 4")
    period4_short = fields.Field(attribute="period4_short", column_name="Short Rebate 4")
    period4_long = fields.Field(attribute="period4_long", column_name="Long Rebate 4")
    period4_high_tea = fields.Field(attribute="period4_high_tea", column_name="High Tea 4")
    period4_bill = fields.Field(attribute="period4_bill", column_name="Bill 4")
    allocation5 = fields.Field(attribute="allocation5", column_name="Allocation for period 5")
    period5_short = fields.Field(attribute="period5_short", column_name="Short Rebate 5")
    period5_long = fields.Field(attribute="period5_long", column_name="Long Rebate 5")
    period5_high_tea = fields.Field(attribute="period5_high_tea", column_name="High Tea 5")
    period5_bill = fields.Field(attribute="period5_bill", column_name="Bill 5")
    allocation6 = fields.Field(attribute="allocation6", column_name="Allocation for period 6")
    period6_short = fields.Field(attribute="period6_short", column_name="Short Rebate 6")
    period6_long = fields.Field(attribute="period6_long", column_name="Long Rebate 6")
    period6_high_tea = fields.Field(attribute="period6_high_tea", column_name="High Tea 6")
    period6_bill = fields.Field(attribute="period6_bill", column_name="Bill 6")
    empty = fields.Field(attribute="empty", column_name="")
    last_sem_fee = fields.Field(attribute="last_sem_fee", column_name="Last Semester Fee")
    total = fields.Field(attribute="total", column_name="Total")
    upcoming_sem_fee = fields.Field(attribute="upcoming_sem_fee", column_name="Upcoming Semester Fee")
    upcoming_sem_due = fields.Field(attribute="upcoming_sem_due", column_name="Upcoming Semester Dues")
    
    def before_import_row(self, row, **kwargs):
    # Convert "TRUE" to True for boolean fields
        for field_name, field_object in self.fields.items():
            if field_object.column_name and field_object.column_name.lower() == "true" or field_object.column_name == 1:
                row[field_name] = True


    def skip_row(self, instance, original, row,import_validation_errors):
        if not instance.email.name and not instance.email.email :
            return True  # Skip the row
        
        return super().skip_row(instance, original, row,import_validation_errors)

    class Meta:
        model = RebateAutumn22
        model = RebateSpring23
        exclude = "id"
        import_id_fields = ["email__email"]
        fields = (
            "email__email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "period1_short",
            "period1_long",
            "period1_high_tea",
            "period1_bill",
            "period2_short",
            "period2_long",
            "period2_high_tea",
            "period2_bill",
            "period3_short",
            "period3_long",
            "period3_high_tea",
            "period3_bill",
            "period4_short",
            "period4_long",
            "period4_high_tea",
            "period4_bill",
            "period5_short",
            "period5_long",
            "period5_high_tea",
            "period5_bill",
            "period6_short",
            "period6_long",
            "period6_high_tea",
            "period6_bill",
            "empty",
            "allocation1",
            "allocation2",
            "allocation3",
            "allocation4",
            "allocation5",
            "allocation6",
            "last_sem_fee",
            "total",
            "upcoming_sem_fee",
            "upcoming_sem_due",
        )
        export_order = (
            "email__email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "empty",
            "allocation1",
            "period1_short",
            "period1_long",
            "period1_high_tea",
            "period1_bill",
            "empty",
            "allocation2",
            "period2_short",
            "period2_long",
            "period2_high_tea",
            "period2_bill",
            "empty",
            "allocation3",
            "period3_short",
            "period3_long",
            "period3_high_tea",
            "period3_bill",
            "empty",
            "allocation4",
            "period4_short",
            "period4_long",
            "period4_high_tea",
            "period4_bill",
            "empty",
            "allocation5",
            "period5_short",
            "period5_long",
            "period5_high_tea",
            "period5_bill",
            "empty",
            "allocation6",
            "period6_short",
            "period6_long",
            "period6_high_tea",
            "period6_bill",
            "empty",
            "last_sem_fee",
            "total",
            "upcoming_sem_fee",
            "upcoming_sem_due",
        )

    def dehydrate_last_sem_fee(self,obj):
        try:
            fee = Fee.objects.get(program=obj.email.degree)
            return fee.prev_sem_fee
        except Exception as e:
            print(e)
            return 0
        
    def dehydrate_upcoming_sem_fee(self,obj):
        try:
            fee = Fee.objects.get(program=obj.email.degree)
            return fee.upcoming_sem_fee
        except Exception as e:
            print(e)
            return 0
    
    def dehydrate_total(self,obj):
        try:
            return obj.period1_bill + obj.period2_bill + obj.period3_bill + obj.period4_bill + obj.period5_bill + obj.period6_bill
        except Exception as e:
            print(e)
            return 0
        
    def dehydrate_upcoming_sem_due(self,obj):
        try:
            fee = Fee.objects.get(program=obj.email.degree)
            return fee.upcoming_sem_fee -(fee.prev_sem_fee - obj.period1_bill - obj.period2_bill - obj.period3_bill - obj.period4_bill - obj.period5_bill - obj.period6_bill)
        except Exception as e:
            print(e)
            return 0
   
    def dehydrate_allocation1(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=1)
            allocation = AllocationSpring23.objects.get(roll_no=obj.email, month=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except Exception as e:
            return "Not yet allocated"
    
    def dehydrate_allocation2(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=2)
            allocation = AllocationSpring23.objects.get(roll_no=obj.email, month=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
    
    def dehydrate_allocation3(self, obj):
        try:
            period = PeriodSpring23.objects.get(Sno=3)
            allocation = AllocationSpring23.objects.get(roll_no=obj.email, month=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation4(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=4)
            allocation = AllocationSpring23.objects.get(roll_no=obj.email, month=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation5(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=5)
            allocation = AllocationSpring23.objects.get(roll_no=obj.email, month=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation6(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=6)
            allocation = AllocationSpring23.objects.get(roll_no=obj.email, month=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"



class StudentBillsResource(resources.ModelResource):
    email__email = fields.Field(
        column_name='Email',
        attribute='email__email',
    )
    email__roll_no = fields.Field(
        attribute="email__roll_no", column_name="Roll No."
    )
    email__name = fields.Field(attribute="email__name", column_name="Name")
    email__department = fields.Field(
        attribute="email__department", column_name="Department"
    )
    email__degree = fields.Field(
        attribute="email__degree", column_name="Academic Program"
    )
    email__hostel = fields.Field(attribute="email__hostel", column_name="Hostel")
    email__room_no = fields.Field(
        attribute="email__room_no", column_name="Room No."
    )
    semester__name = fields.Field(attribute="semester__name", column_name="Semester")
    allocation1 = fields.Field(attribute="allocation1", column_name="Allocation for period 1")
    period1_short = fields.Field(attribute="period1_short", column_name="Short Rebate 1")
    period1_long = fields.Field(attribute="period1_long", column_name="Long Rebate 1")
    period1_high_tea = fields.Field(attribute="period1_high_tea", column_name="High Tea 1")
    period1_bill = fields.Field(attribute="period1_bill", column_name="Bill 1")
    allocation2 = fields.Field(attribute="allocation2", column_name="Allocation for period 2")
    period2_short = fields.Field(attribute="period2_short", column_name="Short Rebate 2")
    period2_long = fields.Field(attribute="period2_long", column_name="Long Rebate 2")
    period2_high_tea = fields.Field(attribute="period2_high_tea", column_name="High Tea 2")
    period2_bill = fields.Field(attribute="period2_bill", column_name="Bill 2")
    allocation3 = fields.Field(attribute="allocation3", column_name="Allocation for period 3")
    period3_short = fields.Field(attribute="period3_short", column_name="Short Rebate 3")
    period3_long = fields.Field(attribute="period3_long", column_name="Long Rebate 3")
    period3_high_tea = fields.Field(attribute="period3_high_tea", column_name="High Tea 3")
    period3_bill = fields.Field(attribute="period3_bill", column_name="Bill 3")
    allocation4 = fields.Field(attribute="allocation4", column_name="Allocation for period 4")
    period4_short = fields.Field(attribute="period4_short", column_name="Short Rebate 4")
    period4_long = fields.Field(attribute="period4_long", column_name="Long Rebate 4")
    period4_high_tea = fields.Field(attribute="period4_high_tea", column_name="High Tea 4")
    period4_bill = fields.Field(attribute="period4_bill", column_name="Bill 4")
    allocation5 = fields.Field(attribute="allocation5", column_name="Allocation for period 5")
    period5_short = fields.Field(attribute="period5_short", column_name="Short Rebate 5")
    period5_long = fields.Field(attribute="period5_long", column_name="Long Rebate 5")
    period5_high_tea = fields.Field(attribute="period5_high_tea", column_name="High Tea 5")
    period5_bill = fields.Field(attribute="period5_bill", column_name="Bill 5")
    allocation6 = fields.Field(attribute="allocation6", column_name="Allocation for period 6")
    period6_short = fields.Field(attribute="period6_short", column_name="Short Rebate 6")
    period6_long = fields.Field(attribute="period6_long", column_name="Long Rebate 6")
    period6_high_tea = fields.Field(attribute="period6_high_tea", column_name="High Tea 6")
    period6_bill = fields.Field(attribute="period6_bill", column_name="Bill 6")
    empty = fields.Field(attribute="empty", column_name="")
    
    def before_import_row(self, row, **kwargs):
    # Convert "TRUE" to True for boolean fields
        for field_name, field_object in self.fields.items():
            if field_object.column_name and field_object.column_name.lower() == "true" or field_object.column_name == 1:
                row[field_name] = True
        


    def skip_row(self, instance, original, row,import_validation_errors):
        if not instance.email.name and not instance.email.email :
            return True  # Skip the row
        
        return super().skip_row(instance, original, row,import_validation_errors)

    class Meta:
        model = StudentBills
        exclude = "id"
        import_id_fields = ["email__email"]
        fields = (
            "email__email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "semester__name",
            "period1_short",
            "period1_long",
            "period1_high_tea",
            "period1_bill",
            "period2_short",
            "period2_long",
            "period2_high_tea",
            "period2_bill",
            "period3_short",
            "period3_long",
            "period3_high_tea",
            "period3_bill",
            "period4_short",
            "period4_long",
            "period4_high_tea",
            "period4_bill",
            "period5_short",
            "period5_long",
            "period5_high_tea",
            "period5_bill",
            "period6_short",
            "period6_long",
            "period6_high_tea",
            "period6_bill",
            "empty",
            "allocation1",
            "allocation2",
            "allocation3",
            "allocation4",
            "allocation5",
            "allocation6",
        )
        export_order = (
            "email__email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "semester__name",
            "empty",
            "allocation1",
            "period1_short",
            "period1_long",
            "period1_high_tea",
            "period1_bill",
            "empty",
            "allocation2",
            "period2_short",
            "period2_long",
            "period2_high_tea",
            "period2_bill",
            "empty",
            "allocation3",
            "period3_short",
            "period3_long",
            "period3_high_tea",
            "period3_bill",
            "empty",
            "allocation4",
            "period4_short",
            "period4_long",
            "period4_high_tea",
            "period4_bill",
            "empty",
            "allocation5",
            "period5_short",
            "period5_long",
            "period5_high_tea",
            "period5_bill",
            "empty",
            "allocation6",
            "period6_short",
            "period6_long",
            "period6_high_tea",
            "period6_bill",
        )

   #Can calculate rebate bills for every function using dehydrate. check commented code in RebateBillsResource

    def dehydrate_allocation1(self,obj):
        try:
            period = Period.objects.get(Sno=1,semester=obj.semester)
            allocation = Allocation.objects.get(roll_no=obj.email, period=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except Exception as e:
            return "Not yet allocated"
    
    def dehydrate_allocation2(self,obj):
        try:
            period = Period.objects.get(Sno=2,semester=obj.semester)
            allocation = Allocation.objects.get(roll_no=obj.email, period=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
    
    def dehydrate_allocation3(self, obj):
        try:
            period = Period.objects.get(Sno=3,semester=obj.semester)
            allocation = Allocation.objects.get(roll_no=obj.email, period=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation4(self,obj):
        try:
            period = Period.objects.get(Sno=4,semester=obj.semester)
            allocation = Allocation.objects.get(roll_no=obj.email, period=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation5(self,obj):
        try:
            period = Period.objects.get(Sno=5,semester=obj.semester)
            allocation = Allocation.objects.get(roll_no=obj.email, period=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation6(self,obj):
        try:
            period = Period.objects.get(Sno=6,semester=obj.semester)
            allocation = Allocation.objects.get(roll_no=obj.email, period=period)
            if(allocation.high_tea): 
                high_tea = "High Tea"
            else:
                high_tea ="No High Tea"
            return str(allocation.caterer_name)+" "+high_tea
        except:
            return "Not yet allocated"

   #Try implementing dehydrate_total function later    
    def dehydrate_total(self,obj):
        return 0


class UnregisteredStudentResource(resources.ModelResource):
    class Meta:
        model = UnregisteredStudent
        exclude = "id"
        import_id_fields = [
            "email",
        ]
        fields = (
            "email",
        )


class CatererBillsNewResource(resources.ModelResource):
    caterer__name = fields.Field(attribute="caterer__name", column_name="Caterer")
    semester__name = fields.Field(attribute="semester__name", column_name="Semester")
    period1_bills = fields.Field(attribute="period1_bills", column_name="Period 1 Bills")
    period2_bills = fields.Field(attribute="period2_bills", column_name="Period 2 Bills")
    period3_bills = fields.Field(attribute="period3_bills", column_name="Period 3 Bills")
    period4_bills = fields.Field(attribute="period4_bills", column_name="Period 4 Bills")
    period5_bills = fields.Field(attribute="period5_bills", column_name="Period 5 Bills")
    period6_bills = fields.Field(attribute="period6_bills", column_name="Period 6 Bills")
    class Meta:
        model = CatererBills
        exclude = "id"
        import_id_fields = [
            "caterer__name",
        ]
        fields = (
            "caterer__name",
            "semester__name",
            "period1_bills",
            "period2_bills",
            "period3_bills",
            "period4_bills",
            "period5_bills",
            "period6_bills",
        )