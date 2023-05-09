from import_export import resources, fields
from .fields import ForeignKeyField
from .models import (
    Student,
    Allocation,
    Rebate,
    LongRebate,
    RebateAutumnSem,
    RebateSpringSem,
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
        attribute="allocation_id__roll_no__name", column_name="Name"
    )
    allocation_id_id__roll_no__roll_no = fields.Field(
        attribute="allocation_id__roll_no__roll_no", column_name="Roll No."
    )
    allocation_id_id__roll_no__department = fields.Field(
        attribute="allocation_id__roll_no__department", column_name="Department"
    )
    allocation_id_id__roll_no__degree = fields.Field(
        attribute="allocation_id__roll_no__degree", column_name="Degree"
    )
    allocation_id_id__roll_no__hostel = fields.Field(
        attribute="allocation_id__roll_no__hostel", column_name="Hostel"
    )
    allocation_id_id__roll_no__room_no = fields.Field(
        attribute="allocation_id__roll_no__room_no", column_name="Room No."
    )
    allocation_id_id__caterer_name = fields.Field(
        attribute="allocation_id__caterer_name", column_name="Caterer Alloted"
    )
    allocation_id_id__high_tea = fields.Field(
        attribute="allocation_id__high_tea", column_name="High Tea"
    )
    date_applied = fields.Field(attribute="date_applied", column_name="date_applied")
    days = fields.Field(attribute="days", column_name="days")
    month = fields.Field(attribute="month", column_name="month")
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
            "date_applied",
            "days",
            "month",
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
            "date_applied",
            "days",
            "month",
            "approved",
        ]


class RebateSpringResource(resources.ModelResource):
    email = fields.Field(attribute="email", column_name="Email")
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

    class Meta:
        model = RebateSpringSem
        exclude = "id"
        import_id_fields = ["email"]
        export_order = [
            "email",
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
        ]
        fields = (
            "email",
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

    # def after_export(self, queryset, data, *args, **kwargs):
    #     amount=130
    #     for row in data:
    #         # row['email'] = row['email'].lower()
    #         if(row['highTeajanuary'] == False):
    #             amount=amount-15
    #             row['januaryBill'] = 31*15
    #         row['januaryBill'] = (row['januaryShort']+row['januaryLong'])*amount
    #         if(row['highTeaFeburary'] == False):
    #             amount=amount-15
    #             row['feburaryBill'] = 28*15
    #         row['feburaryBill'] = (row['feburaryShort']+row['feburaryLong'])*amount
    #         if(row['highTeaMarch'] == False):
    #             amount=amount-15
    #             row['marchBill'] = 31*15
    #         row['marchBill'] = (row['marchShort']+row['marchLong'])*amount
    #         if(row['highTeaApril'] == False):
    #             amount=amount-15
    #             row['aprilBill'] = 30*15
    #         row['aprilBill'] = (row['aprilShort']+row['aprilLong'])*amount
    #         if(row['highTeaMay'] == False):
    #             amount=amount-15
    #             row['mayBill'] = 31*15
    #         row['mayBill'] = (row['mayShort']+row['mayLong'])*amount
    #         if(row['highTeaJune'] == False):
    #             amount=amount-15
    #             row['juneBill'] = 30*15
    #        row['juneBill'] = (row['juneShort']+row['juneLong'])*amount
    # row['total'] = row['januaryBill']+row['feburaryBill']+row['marchBill']+row['aprilBill']+row['mayBill']+row['juneBill']

    # def dehydrate(self, row):
    #     print(row)
    #     AprBill_val = 2
    #     row.update({'AprBill': AprBill_val})
    #     MayBill_val = row.mayShort * 2
    #     row.update({'MayBill': MayBill_val})
    #     return row


class RebateAutumnResource(resources.ModelResource):
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

    class Meta:
        model = RebateAutumnSem
        exclude = "id"
        import_id_fields = ["email"]
        export_order = [
            "email",
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
        ]
        fields = (
            "email",
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
