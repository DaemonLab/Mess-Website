from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    Student,
    Allocation,
    Rebate,
    LongRebate,
    UnregisteredStudent,
    RebateSpring23,
    RebateAutumn23,
    RebateAutumn22,
    PeriodSpring23,
    PeriodAutumn23,
    PeriodAutumn22,
    AllocationAutumn22,
    AllocationSpring23,
    AllocationAutumn23,
)

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
            "name",
            "email",
            "roll_no",
            "hostel",
            "room_no",
            "degree",
            "department",
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


class AllocationResource(resources.ModelResource):
    roll_no__roll_no = fields.Field(
        attribute="roll_no__roll_no", column_name="Roll No."
    )
    roll_no__email = fields.Field(attribute="roll_no__email", column_name="Email")
    roll_no__name = fields.Field(attribute="roll_no__name", column_name="Name")
    roll_no__department = fields.Field(
        attribute="roll_no__department", column_name="Department"
    )
    roll_no__degree = fields.Field(
        attribute="roll_no__degree", column_name="Academic Program"
    )
    roll_no__hostel = fields.Field(attribute="roll_no__hostel", column_name="Hostel")
    roll_no__room_no = fields.Field(
        attribute="roll_no__room_no", column_name="Room No."
    )
    month = fields.Field(attribute="month", column_name="Month")
    student_id = fields.Field(attribute="student_id", column_name="Student ID")
    caterer_name = fields.Field(attribute="caterer_name", column_name="Caterer Alloted")
    high_tea = fields.Field(attribute="high_tea", column_name="High Tea")
    first_pref = fields.Field(attribute="first_pref", column_name="First Preferences")
    second_pref = fields.Field(
        attribute="second_pref", column_name="Second Preferences"
    )
    third_pref = fields.Field(attribute="third_pref", column_name="Third Preferences")

    class Meta:
        model = Allocation
        fields = (
            "roll_no__roll_no",
            "roll_no__email",
            "roll_no__name",
            "roll_no__department",
            "roll_no__degree",
            "roll_no__hostel",
            "roll_no__room_no",
            "month",
            "student_id",
            "caterer_name",
            "high_tea",
            "first_pref",
            "second_pref",
            "third_pref",
        )

        export_order = [
            "roll_no__roll_no",
            "roll_no__email",
            "roll_no__name",
            "roll_no__department",
            "roll_no__degree",
            "roll_no__hostel",
            "roll_no__room_no",
            "month",
            "student_id",
            "caterer_name",
            "high_tea",
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
    email = fields.Field(attribute="email", column_name="Email")
    allocation_id_id__roll_no__name = fields.Field(
        attribute="allocation_id_id__roll_no__name", column_name="Name"
    )
    allocation_id_id__roll_no__roll_no = fields.Field(
        attribute="allocation_id_id__roll_no__roll_no", column_name="Roll No."
    )
    allocation_id_id__roll_no__department = fields.Field(
        attribute="allocation_id_id__roll_no__department", column_name="Department"
    )
    allocation_id_id__roll_no__degree = fields.Field(
        attribute="allocation_id_id__roll_no__degree", column_name="Degree"
    )
    allocation_id_id__roll_no__hostel = fields.Field(
        attribute="allocation_id_id__roll_no__hostel", column_name="Hostel"
    )
    allocation_id_id__roll_no__room_no = fields.Field(
        attribute="allocation_id_id__roll_no__room_no", column_name="Room No."
    )
    allocation_id_id__caterer_name = fields.Field(
        attribute="allocation_id_id__caterer_name", column_name="Caterer Alloted"
    )
    allocation_id_id__high_tea = fields.Field(
        attribute="allocation_id_id__high_tea", column_name="High Tea"
    )
    date_applied = fields.Field(attribute="date_applied", column_name="date_applied")
    days = fields.Field(attribute="days", column_name="days")
    month = fields.Field(attribute="month", column_name="month")
    approved = fields.Field(attribute="approved", column_name="Approved")

    class Meta:
        model = LongRebate
        fields = (
            "email",
            "allocation_id_id__roll_no__name",
            "allocation_id_id__roll_no__roll_no",
            "allocation_id_id__roll_no__department",
            "allocation_id_id__roll_no__degree",
            "allocation_id_id__roll_no__hostel",
            "allocation_id_id__roll_no__room_no",
            "allocation_id_id__high_tea",
            "allocation_id_id__caterer_name",
            "date_applied",
            "days",
            "month",
            "approved",
        )
        export_order = [
            "email",
            "allocation_id_id__roll_no__name",
            "allocation_id_id__roll_no__roll_no",
            "allocation_id_id__roll_no__department",
            "allocation_id_id__roll_no__degree",
            "allocation_id_id__roll_no__hostel",
            "allocation_id_id__roll_no__room_no",
            "allocation_id_id__high_tea",
            "allocation_id_id__caterer_name",
            "date_applied",
            "days",
            "month",
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
    period1_short = fields.Field(attribute="period1_short", column_name="Short Rebate")
    period1_long = fields.Field(attribute="period1_long", column_name="Long Rebate")
    period1_high_tea = fields.Field(attribute="period1_high_tea", column_name="High Tea")
    period1_bill = fields.Field(attribute="period1_bill", column_name="Bill")
    allocation2 = fields.Field(attribute="allocation2", column_name="Allocation for period 2")
    period2_short = fields.Field(attribute="period2_short", column_name="Short Rebate")
    period2_long = fields.Field(attribute="period2_long", column_name="Long Rebate")
    period2_high_tea = fields.Field(attribute="period2_high_tea", column_name="High Tea")
    period2_bill = fields.Field(attribute="period2_bill", column_name="Bill")
    allocation3 = fields.Field(attribute="allocation3", column_name="Allocation for period 3")
    period3_short = fields.Field(attribute="period3_short", column_name="Short Rebate")
    period3_long = fields.Field(attribute="period3_long", column_name="Long Rebate")
    period3_high_tea = fields.Field(attribute="period3_high_tea", column_name="High Tea")
    period3_bill = fields.Field(attribute="period3_bill", column_name="Bill")
    allocation4 = fields.Field(attribute="allocation4", column_name="Allocation for period 4")
    period4_short = fields.Field(attribute="period4_short", column_name="Short Rebate")
    period4_long = fields.Field(attribute="period4_long", column_name="Long Rebate")
    period4_high_tea = fields.Field(attribute="period4_high_tea", column_name="High Tea")
    period4_bill = fields.Field(attribute="period4_bill", column_name="Bill")
    allocation5 = fields.Field(attribute="allocation5", column_name="Allocation for period 5")
    period5_short = fields.Field(attribute="period5_short", column_name="Short Rebate")
    period5_long = fields.Field(attribute="period5_long", column_name="Long Rebate")
    period5_high_tea = fields.Field(attribute="period5_high_tea", column_name="High Tea")
    period5_bill = fields.Field(attribute="period5_bill", column_name="Bill")
    allocation6 = fields.Field(attribute="allocation6", column_name="Allocation for period 6")
    period6_short = fields.Field(attribute="period6_short", column_name="Short Rebate")
    period6_long = fields.Field(attribute="period6_long", column_name="Long Rebate")
    period6_high_tea = fields.Field(attribute="period6_high_tea", column_name="High Tea")
    period6_bill = fields.Field(attribute="period6_bill", column_name="Bill")
    empty = fields.Field(attribute="empty", column_name="")
    
    class Meta:
        model = RebateAutumn22
        model = RebateAutumn23
        model = RebateSpring23
        exclude = "id"
        import_id_fields = ["email_email"]
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
        )

    obj = RebateAutumn22.objects.all()
    def dehydrate_empty(self, obj):
        return ""
        
    def dehydrate_period1_bill(self, obj):
        amount=130
        period1_bill=0
        if(obj.period1_high_tea == False):
            amount=amount-15
            period1_bill = 31*15
        period1_bill += (int(obj.period1_short)+int(obj.period1_long))*int(amount)
        return period1_bill
    
    def dehydrate_period2_bill(self, obj):
        amount=130
        period2_bill=0
        if(obj.period2_high_tea == False):
            amount=amount-15
            period2_bill = 31*15
        period2_bill += (int(obj.period2_short)+int(obj.period2_long))*int(amount)
        return period2_bill
    
    def dehydrate_period3_bill(self, obj):
        amount=130
        period3_bill=0
        if(obj.period3_high_tea == False):
            amount=amount-15
            period3_bill = 31*15
        period3_bill += (int(obj.period3_short)+int(obj.period3_long))*int(amount)
        return period3_bill
    
    def dehydrate_period4_bill(self, obj):
        amount=130
        period4_bill=0
        if(obj.period4_high_tea == False):
            amount=amount-15
            period4_bill = 31*15
        period4_bill += (int(obj.period4_short)+int(obj.period4_long))*int(amount)
        return period4_bill
    
    def dehydrate_period5_bill(self, obj):
        amount=130
        period5_bill=0
        if(obj.period5_high_tea == False):
            amount=amount-15
            period5_bill = 31*15
        period5_bill += (int(obj.period5_short)+int(obj.period5_long))*int(amount)
        return period5_bill
    
    def dehydrate_period6_bill(self, obj):
        amount=130
        period6_bill=0
        if(obj.period6_high_tea == False):
            amount=amount-15
            period6_bill = 31*15
        period6_bill += (int(obj.period6_short)+int(obj.period6_long))*int(amount)
        return period6_bill
    
    def dehydrate_allocation1(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=1)
            allocation = AllocationSpring23.objects.get(email=obj.email.email, month=period)
            return str(allocation.caterer_name)+" "+str(allocation.high_tea)
        except Exception as e:
            return "Not yet allocated"
    
    def dehydrate_allocation2(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=2)
            allocation = AllocationSpring23.objects.get(email=obj.email.email, month=period)
            return str(allocation.caterer_name)+" "+str(allocation.high_tea)
        except:
            return "Not yet allocated"
    
    def dehydrate_allocation3(self, obj):
        try:
            period = PeriodSpring23.objects.get(Sno=3)
            allocation = AllocationSpring23.objects.get(email=obj.email.email, month=period)
            return str(allocation.caterer_name)+" "+str(allocation.high_tea)
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation4(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=4)
            allocation = AllocationSpring23.objects.get(email=obj.email.email, month=period)
            return str(allocation.caterer_name)+" "+str(allocation.high_tea)
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation5(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=5)
            allocation = AllocationSpring23.objects.get(email=obj.email.email, month=period)
            return str(allocation.caterer_name)+" "+str(allocation.high_tea)
        except:
            return "Not yet allocated"
        
    def dehydrate_allocation6(self,obj):
        try:
            period = PeriodSpring23.objects.get(Sno=6)
            allocation = AllocationSpring23.objects.get(email=obj.email.email, month=period)
            return str(allocation.caterer_name)+" "+str(allocation.high_tea)
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

