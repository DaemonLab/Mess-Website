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


class RebateSpringResource(resources.ModelResource):
    email = fields.Field(
        column_name='Email',
        attribute='email',
        widget=ForeignKeyWidget(Student, field='email')
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
    januaryShort = fields.Field(attribute="januaryShort", column_name="January Short")
    januaryLong = fields.Field(attribute="januaryLong", column_name="January Long")
    highTeaJanuary = fields.Field(
        attribute="highTeaJanuary", column_name="High Tea January"
    )
    januaryBill = fields.Field(attribute="januaryBill", column_name="January Bill")
    feburaryShort = fields.Field(
        attribute="feburaryShort", column_name="Feburary Short"
    )
    feburaryLong = fields.Field(attribute="feburaryLong", column_name="Feburary Long")
    highTeaFeburary = fields.Field(
        attribute="highTeaFeburary", column_name="High Tea Feburary"
    )
    feburaryBill = fields.Field(attribute="feburaryBill", column_name="Feburary Bill")
    marchShort = fields.Field(attribute="marchShort", column_name="March Short")
    marchLong = fields.Field(attribute="marchLong", column_name="March Long")
    highTeaMarch = fields.Field(attribute="highTeaMarch", column_name="High Tea March")
    marchBill = fields.Field(attribute="marchBill", column_name="March Bill")
    aprilShort = fields.Field(attribute="aprilShort", column_name="April Short")
    aprilLong = fields.Field(attribute="aprilLong", column_name="April Long")
    highTeaApril = fields.Field(attribute="highTeaApril", column_name="High Tea April")
    aprilBill = fields.Field(attribute="aprilBill", column_name="April Bill")
    mayShort = fields.Field(attribute="mayShort", column_name="May Short")
    mayLong = fields.Field(attribute="mayLong", column_name="May Long")
    highTeaMay = fields.Field(attribute="highTeaMay", column_name="High Tea May")
    mayBill = fields.Field(attribute="mayBill", column_name="May Bill")
    juneShort = fields.Field(attribute="juneShort", column_name="June Short")
    juneLong = fields.Field(attribute="juneLong", column_name="June Long")
    highTeaJune = fields.Field(attribute="highTeaJune", column_name="High Tea June")
    juneBill = fields.Field(attribute="juneBill", column_name="June Bill")
    empty = fields.Field(column_name=" ")

    class Meta:
        model = RebateSpring23
        exclude = "id"
        import_id_fields = ["email",]
        export_order = [
            "email__roll_no",
            "email",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "januaryShort",
            "januaryLong",
            "highTeaJanuary",
            "januaryBill",
            "empty",
            "feburaryShort",
            "feburaryLong",
            "highTeaFeburary",
            "feburaryBill",
            "empty",
            "marchShort",
            "marchLong",
            "highTeaMarch",
            "marchBill",
            "empty",
            "aprilShort",
            "aprilLong",
            "highTeaApril",
            "aprilBill",
            "empty",
            "mayShort",
            "mayLong",
            "highTeaMay",
            "mayBill",
            "empty",
            "juneShort",
            "juneLong",
            "highTeaJune",
            "juneBill",
        ]
        fields = (
            "email",
            "email__roll_no",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "januaryShort",
            "januaryLong",
            "highTeaJanuary",
            "januaryBill",
            "feburaryShort",
            "feburaryLong",
            "highTeaFeburary",
            "feburaryBill",
            "marchShort",
            "marchLong",
            "highTeaMarch",
            "marchBill",
            "aprilShort",
            "aprilLong",
            "highTeaApril",
            "aprilBill",
            "mayShort",
            "mayLong",
            "highTeaMay",
            "mayBill",
            "juneShort",
            "juneLong",
            "highTeaJune",
            "juneBill",
        )

        # row['total'] = row['januaryBill']+row['feburaryBill']+row['marchBill']+row['aprilBill']+row['mayBill']+row['juneBill']
        def before_import_rom(self,row, **kwargs):
            email=row.get('email')
            email=Student.objects.get(email=email)
            row['email']=email

    def dehydrate_januaryBill(self, RebateSpringSem):
        amount=130
        januaryBill = 0
        if(RebateSpringSem.highTeaJanuary == False):
            amount=amount-15
            januaryBill = 31*15 
        januaryBill += (int(RebateSpringSem.januaryShort)+int(RebateSpringSem.januaryLong))*int(amount)
        return januaryBill
    
    def dehydrate_feburaryBill(self, RebateSpringSem):
        amount=130
        feburaryBill = 0
        if(RebateSpringSem.highTeaFeburary == False):
            amount=amount-15
            feburaryBill = 28*15 
        feburaryBill += (int(RebateSpringSem.feburaryShort)+int(RebateSpringSem.feburaryLong))*int(amount)
        return feburaryBill
    
    def dehydrate_marchBill(self, RebateSpringSem):
        amount=130
        marchBill = 0
        if(RebateSpringSem.highTeaMarch == False):
            amount=amount-15
            marchBill = 31*15 
        marchBill += (int(RebateSpringSem.marchShort)+int(RebateSpringSem.marchLong))*int(amount)
        return marchBill
    
    def dehydrate_aprilBill(self, RebateSpringSem):
        amount=130
        aprilBill = 0
        if(RebateSpringSem.highTeaApril == False):
            amount=amount-15
            aprilBill = 30*15 
        aprilBill += (int(RebateSpringSem.aprilShort)+int(RebateSpringSem.aprilLong))*int(amount)
        return aprilBill
    
    def dehydrate_mayBill(self, RebateSpringSem):
        amount=130
        mayBill = 0
        if(RebateSpringSem.highTeaMay == False):
            amount=amount-15
            mayBill = 31*15 
        mayBill += (int(RebateSpringSem.mayShort)+int(RebateSpringSem.mayLong))*int(amount)
        return mayBill
    
    def dehydrate_juneBill(self, RebateSpringSem):
        amount=130
        juneBill = 0
        if(RebateSpringSem.highTeaJune == False):
            amount=amount-15
            juneBill = 30*15 
        juneBill += (int(RebateSpringSem.juneShort)+int(RebateSpringSem.juneLong))*int(amount)
        return juneBill

    #Try implementing dehydrate_total function later    

class RebateAutumnResource(resources.ModelResource):
    email = fields.Field(
        column_name='Email',
        attribute='email',
        widget=ForeignKeyWidget(Student, field='email')
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
    julyShort = fields.Field(attribute="julyShort", column_name="July Short")
    julyLong = fields.Field(attribute="julyLong", column_name="July Long")
    highTeaJuly = fields.Field(attribute="highTeaJuly", column_name="High Tea July")
    julyBill = fields.Field(attribute="julyBill", column_name="July Bill")
    augustShort = fields.Field(attribute="augustShort", column_name="August Short")
    augustLong = fields.Field(attribute="augustLong", column_name="August Long")
    highTeaAugust = fields.Field(
        attribute="highTeaAugust", column_name="High Tea August"
    )
    augustBill = fields.Field(attribute="augustBill", column_name="August Bill")
    septemberShort = fields.Field(
        attribute="septemberShort", column_name="September Short"
    )
    septemberLong = fields.Field(
        attribute="septemberLong", column_name="September Long"
    )
    highTeaSeptember = fields.Field(
        attribute="highTeaSeptember", column_name="High Tea September"
    )
    septemberBill = fields.Field(
        attribute="septemberBill", column_name="September Bill"
    )
    octoberShort = fields.Field(attribute="octoberShort", column_name="October Short")
    octoberLong = fields.Field(attribute="octoberLong", column_name="October Long")
    highTeaOctober = fields.Field(
        attribute="highTeaOctober", column_name="High Tea October"
    )
    octoberBill = fields.Field(attribute="octoberBill", column_name="October Bill")
    novemberShort = fields.Field(
        attribute="novemberShort", column_name="November Short"
    )
    novemberLong = fields.Field(attribute="novemberLong", column_name="November Long")
    highTeaNovember = fields.Field(
        attribute="highTeaNovember", column_name="High Tea November"
    )
    novemberBill = fields.Field(attribute="novemberBill", column_name="November Bill")
    decemberShort = fields.Field(
        attribute="decemberShort", column_name="December Short"
    )
    decemberLong = fields.Field(attribute="decemberLong", column_name="December Long")
    highTeaDecember = fields.Field(
        attribute="highTeaDecember", column_name="High Tea December"
    )
    decemberBill = fields.Field(attribute="decemberBill", column_name="December Bill")
    empty = fields.Field(column_name=" ")

    class Meta:
        model = RebateAutumn23
        exclude = "id"
        import_id_fields = ["email__email",]
        export_order = [
            "email__roll_no",
            "email",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "julyShort",
            "julyLong",
            "highTeaJuly",
            "julyBill",
            "empty",
            "augustShort",
            "augustLong",
            "highTeaAugust",
            "augustBill",
            "empty",
            "septemberShort",
            "septemberLong",
            "highTeaSeptember",
            "septemberBill",
            "empty",
            "octoberShort",
            "octoberLong",
            "highTeaOctober",
            "octoberBill",
            "empty",
            "novemberShort",
            "novemberLong",
            "highTeaNovember",
            "NovemberBill",
            "empty",
            "decemberShort",
            "decemberLong",
            "highTeaDecember",
            "decemberBill",
            "empty"
        ]
        fields = (
            "email__roll_no",
            "email",
            "email__name",
            "email__department",
            "email__degree",
            "email__hostel",
            "email__room_no",
            "julyShort",
            "julyLong",
            "highTeaJuly",
            "julyBill",
            "augustShort",
            "augustLong",
            "highTeaAugust",
            "augustBill",
            "septemberShort",
            "septemberLong",
            "highTeaSeptember",
            "septemberBill",
            "octoberShort",
            "octoberLong",
            "highTeaOctober",
            "octoberBill",
            "novemberShort",
            "novemberLong",
            "highTeaNovember",
            "NovemberBill",
            "decemberShort",
            "decemberLong",
            "highTeaDecember",
            "decemberBill",
        )
        def before_import_rom(self,row, **kwargs):
            email=row.get('email')
            email=Student.objects.get(email=email)
            row['email']=email

    def dehydrate_julyBill(self, RebateAutumnSem):
        amount=130
        julyBill = 0
        if(RebateAutumnSem.highTeaJuly == False):
            amount=amount-15
            julyBill = 31*15 
        julyBill += (int(RebateAutumnSem.julyShort)+int(RebateAutumnSem.julyLong))*int(amount)
        return julyBill
    
    def dehydrate_augustBill(self, RebateAutumnSem):
        amount=130
        augustBill = 0
        if(RebateAutumnSem.highTeaAugust == False):
            amount=amount-15
            augustBill = 31*15 
        augustBill += (int(RebateAutumnSem.augustShort)+int(RebateAutumnSem.augustLong))*int(amount)
        return augustBill
    
    def dehydrate_septemberBill(self, RebateAutumnSem):
        amount=130
        septemberBill = 0
        if(RebateAutumnSem.highTeaSeptember == False):
            amount=amount-15
            septemberBill = 30*15 
        septemberBill += (int(RebateAutumnSem.septemberShort)+int(RebateAutumnSem.septemberLong))*int(amount)
        return septemberBill
    
    def dehydrate_octoberBill(self, RebateAutumnSem):
        amount=130
        octoberBill = 0
        if(RebateAutumnSem.highTeaOctober == False):
            amount=amount-15
            octoberBill = 31*15 
        octoberBill += (int(RebateAutumnSem.octoberShort)+int(RebateAutumnSem.octoberLong))*int(amount)
        return octoberBill
    
    def dehydrate_novemberBill(self, RebateAutumnSem):
        amount=130
        novemberBill = 0
        if(RebateAutumnSem.highTeaNovember == False):
            amount=amount-15
            novemberBill = 30*15 
        novemberBill += (int(RebateAutumnSem.novemberShort)+int(RebateAutumnSem.novemberLong))*int(amount)
        return novemberBill
    
    def dehydrate_decemberBill(self, RebateAutumnSem):
        amount=130
        decemberBill = 0
        if(RebateAutumnSem.highTeaDecember == False):
            amount=amount-15
            decemberBill = 31*15 
        decemberBill += (int(RebateAutumnSem.decemberShort)+int(RebateAutumnSem.decemberLong))*int(amount)
        return decemberBill
    

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

