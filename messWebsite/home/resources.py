from import_export import resources, fields
from .fields import ForeignKeyField
from .models import(
    Student,
    Allocation,
    Rebate
)

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        exclude='id'
        import_id_fields = ['name', 'email','roll_no', "hostel", "room_no", "degree", "department"]
        fields = ('name', 'email','roll_no', "hostel", "room_no", "degree", "department")

class AllocationResource(resources.ModelResource):
    roll_no = ForeignKeyField(attribute='roll_no', column='roll_no')
    roll_no = fields.Field(attribute="roll_no", column_name="Roll No.")
    roll_no__name = fields.Field(attribute="roll_no__name", column_name="Name")
    roll_no__department = fields.Field(attribute="roll_no__department", column_name="Department")
    roll_no__degree = fields.Field(attribute="roll_no__degree", column_name="Degree")
    roll_no__hostel = fields.Field(attribute="roll_no__hostel", column_name="Hostel")
    roll_no__room_no = fields.Field(attribute="roll_no__room_no", column_name="Room No.")
    month = fields.Field(attribute="month", column_name="Month")
    student_id = fields.Field(attribute="student_id", column_name="Student ID")
    caterer_name = fields.Field(attribute="caterer_name", column_name="Caterer Alloted")
    high_tea = fields.Field(attribute="high_tea", column_name="High Tea")
    first_pref = fields.Field(attribute="first_pref", column_name="First Preferences")
    second_pref = fields.Field(attribute="second_pref", column_name="Second Preferences")
    third_pref = fields.Field(attribute="third_pref", column_name="Third Preferences")

    class Meta:
        model = Allocation
        fields = ("roll_no",
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
                    "third_pref")
        
        export_order = ["roll_no",
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
                    "third_pref"]

class RebateResource(resources.ModelResource):
    allocation_id = ForeignKeyField(attribute='allocation_id', column='student_id')
    # def get_approved_value(self, obj):
    #     if obj.approved:
    #         return "Yes"
    #     else:
    #         return "No"

    # approved = fields.Field(
    #     attribute='get_approved_value',
    #     column_name='approved'
    # )

    email = fields.Field(attribute="email", column_name="Email")
    allocation_id__roll_no__name = fields.Field(attribute="allocation_id__roll_no__name", column_name="Name")
    allocation_id__roll_no__roll_no = fields.Field(attribute="allocation_id__roll_no__roll_no", column_name="Roll No.")
    allocation_id__roll_no__department = fields.Field(attribute="allocation_id__roll_no__department", column_name="Department")
    allocation_id__roll_no__degree = fields.Field(attribute="allocation_id__roll_no__degree", column_name="Degree")
    allocation_id__roll_no__hostel = fields.Field(attribute="allocation_id__roll_no__hostel", column_name="Hostel")
    allocation_id__roll_no__room_no = fields.Field(attribute="allocation_id__roll_no__room_no", column_name="Room No.")
    allocation_id = fields.Field(attribute="allocation_id", column_name="Student ID")
    allocation_id__caterer_name = fields.Field(attribute="allocation_id__caterer_name", column_name="Caterer Alloted")
    allocation_id__high_tea = fields.Field(attribute="allocation_id__high_tea", column_name="High Tea")
    date_applied = fields.Field(attribute="date_applied", column_name="date_applied")
    start_date = fields.Field(attribute="start_date", column_name="Start Date")
    end_date = fields.Field(attribute="end_date", column_name="End Date")
    approved = fields.Field(attribute="approved", column_name="Approved")
    
    class Meta:
        model = Rebate
        fields = (  "email",
                    "allocation_id__roll_no__name",
                    "allocation_id__roll_no__roll_no",
                    "allocation_id__roll_no__department",
                    "allocation_id__roll_no__degree",
                    "allocation_id__roll_no__hostel",
                    "allocation_id__roll_no__room_no",
                    "allocation_id__high_tea",
                    "allocation_id__caterer_name",
                    "allocation_id",
                    "date_applied",
                    "start_date",
                    "end_date",
                    "approved",)
        export_order = ["email",
                        "allocation_id__roll_no__name",
                        "allocation_id__roll_no__roll_no",
                        "allocation_id__roll_no__department",
                        "allocation_id__roll_no__degree",
                        "allocation_id__roll_no__hostel",
                        "allocation_id__roll_no__room_no",
                        "allocation_id",
                        "date_applied",
                        "start_date",
                        "end_date",
                        "approved",]