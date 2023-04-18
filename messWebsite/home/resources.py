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
    
    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'roll_no':
                headers[i] = "Roll No."
            if h == 'roll_no__name':
                headers[i] = "Name"
            if h == 'roll_no__department':
                headers[i] = "Department"
            if h == 'roll_no__degree':
                headers[i] = "Degree"
            if h == 'roll_no__hostel':
                headers[i] = "Hostel"
            if h == 'roll_no__room_no':
                headers[i] = "Room No."
            if h == 'month':
                headers[i] = "Month"
            if h == 'student_id':
                headers[i] = "Allocation ID"
            if h == 'caterer_name':
                headers[i] = "Caterer"
            if h == 'high_tea':
                headers[i] = "High Tea"
            if h == 'first_pref':
                headers[i] = "First Preference"
            if h == 'second_pref':
                headers[i] = "Second Preference"
        return headers

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

    class Meta:
        model = Rebate
        fields = (  "email",
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
                    "approved",)