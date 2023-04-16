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
        fields = ('name', 'email','roll_no', "hostel", "room_no", "degree", "department")

class AllocationResource(resources.ModelResource):
    roll_no = ForeignKeyField(attribute='roll_no', column='roll_no')

    class Meta:
        model = Allocation
        fields = ("roll_no",
                    "month",
                    "student_id",
                    "caterer_name",
                    "high_tea",
                    "first_pref",
                    "second_pref",
                    "third_pref")

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

    class Meta:
        model = Rebate
        fields = (  "email",
                    "allocation_id",
                    "date_applied",
                    "start_date",
                    "end_date",
                    "approved",)