"""
File-name: admin.py
This file is registers the models on the adming page and customizes the admin page
For more information please see: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
"""

import csv
from datetime import timedelta

from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from import_export.admin import ImportExportMixin, ImportExportModelAdmin

from home.models import (
    About,
    Allocation,
    AllocationForm,
    Cafeteria,
    Carousel,
    Caterer,
    CatererBills,
    Contact,
    Fee,
    Form,
    LeftLongRebate,
    LeftShortRebate,
    LongRebate,
    Period,
    Rebate,
    Rule,
    Scan,
    Semester,
    Student,
    StudentBills,
    UnregisteredStudent,
    Update,
)
from home.utils.rebate_checker import max_days_rebate

from .resources import (
    AllocationResource,
    CatererBillsResource,
    LongRebateResource,
    RebateResource,
    StudentBillsResource,
    StudentResource,
    UnregisteredStudentResource,
)
from .utils.django_email_server import long_rebate_query_mail
from .utils.month import fill_periods, map_periods_to_long_rebate
from .utils.rebate_bills_saver import fix_all_bills, save_long_bill

# Customising the heading and title of the admin page
admin.site.site_header = "Dining Website Admin Page"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Website Admin panel"


# Text of description content of each model
ABOUT_DESC_TEXT = "This contains the content that will show up in the about section of the home page. Add all of the About us Content in one field itself."
CAROUSEL_DESC_TEXT = "This contains the images that will show up in the carousel of the home page. Add new field for each new image."
UPDATE_DESC_TEXT = "This contains the content that will show up in the update section of the home page. Add new field for each new update."
PHOTOS_DESC_TEXT = "This contains the photographs that will show up in the bottom section of the home page. Add new field for each new image."
RULE_DESC_TEXT = "This contains the content that will show up in the rule section of the Rules page. Add new field for each new rule."
PENALTY_DESC_TEXT = "This contains the content that will show up in the penalty section of the Rules page. Add new field for each new penalty."
SHORT_REBATE_DESC_TEXT = "This contains the content that will show up in the short rebate section of the rules page. Add all of the short term rebate Content in one field itself."
LONG_REBATE_DESC_TEXT = "This contains the content that will show up in the rule section of the Rules page. Add new field for each new rule."
CATERER_DESC_TEXT = "This contains the content that will show up in the respective caterers page. Add new field for each new caterer."
FORM_DESC_TEXT = "This contains the content that will show up in the forms page. Add new field for each new form data."
CAFETERIA_DESC_TEXT = "This contains the content that will show up in the Additional Service page. Add new field for each new Service."
CONTACT_DESC_TEXT = "This contains the content that will show up in the contact page. Add new field for each new contact."
ALLOCATION_DESC_TEXT = "This contains the Allocation details of the students. First import data through /allocation/ url then export"
STUDENT_DESC_TEXT = "This contains the Basic details of each students."
REBATE_DESC_TEXT = (
    "This contains the rebate details of each rebate applied by the students."
)
REBATE_BILLS_DESC_TEXT = "This contains the rebate bills of each students."

# Register your models here


@admin.register(About)
class about_Admin(admin.ModelAdmin):
    model = About
    fieldsets = (
        (
            None,
            {
                "fields": ("description",),
                "description": "%s" % ABOUT_DESC_TEXT,
            },
        ),
    )


@admin.register(Carousel)
class about_Admin(admin.ModelAdmin):
    model = Carousel
    fieldsets = (
        (
            None,
            {
                "fields": ("image",),
                "description": "%s" % CAROUSEL_DESC_TEXT,
            },
        ),
    )


@admin.register(Update)
class about_Admin(admin.ModelAdmin):
    model = Update
    ordering = ("-time_stamp",)
    search_fields = ("update", "time_stamp")
    list_filter = ("time_stamp",)
    fieldsets = (
        (
            None,
            {
                "fields": ("update",),
                "description": "%s" % UPDATE_DESC_TEXT,
            },
        ),
    )


@admin.register(Rule)
class about_Admin(admin.ModelAdmin):
    model = Rule
    ordering = ("rule",)
    search_fields = ("rule",)
    list_display = ("rule",)
    list_filter = ("rule",)
    fieldsets = (
        (
            None,
            {
                "fields": ("rule",),
                "description": "%s" % RULE_DESC_TEXT,
            },
        ),
    )


@admin.register(Caterer)
class CatererAdmin(admin.ModelAdmin):
    model = Caterer
    search_fields = ("name",)
    list_filter = (
        "id",
        "name",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "upper_description",
                    "sheet_url",
                    "lower_description",
                    "student_limit",
                    "visible",
                ),
                "description": "%s" % CATERER_DESC_TEXT,
            },
        ),
    )
    # In future can create an admin action to directly generate the table for caterer v=bills for a semester.
    actions = ["generate_table"]

    @admin.action(description="Generate the table for caterer Bills")
    def generate_table(self, request, queryset):
        semester = Semester.objects.filter().last()
        for caterer in queryset:
            caterer_bill, _ = CatererBills.objects.get_or_create(
                caterer=caterer, semester=semester
            )
            caterer_bill.save()


@admin.register(Form)
class about_Admin(admin.ModelAdmin):
    model = Form
    search_fields = ("heading", "description")
    list_filter = ("heading",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "heading",
                    "url",
                    "description",
                ),
                "description": "%s" % FORM_DESC_TEXT,
            },
        ),
    )


@admin.register(Cafeteria)
class about_Admin(admin.ModelAdmin):
    model = Cafeteria
    search_fields = ("name", "poc")
    list_filter = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "poc",
                    "contact",
                    "image",
                ),
                "description": "%s" % CAFETERIA_DESC_TEXT,
            },
        ),
    )


@admin.register(Contact)
class about_Admin(admin.ModelAdmin):
    model = Contact
    search_fields = ("occupation", "name", "hostel_sec")
    list_filter = ("occupation", "hostel_sec")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("occupation", "hostel_sec"),
                    "name",
                    "contact",
                    "email",
                ),
                "description": "%s" % CONTACT_DESC_TEXT,
            },
        ),
    )


@admin.register(Student)
class about_Admin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    model = Student
    search_fields = ("name", "roll_no", "hostel", "degree", "department", "email")
    list_display = ("name", "roll_no", "hostel", "email", "allocation_enabled")
    list_filter = ("hostel", "degree", "department")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "roll_no",
                    "hostel",
                    "room_no",
                    "degree",
                    "department",
                    "allocation_enabled",
                ),
                "description": "%s" % STUDENT_DESC_TEXT,
            },
        ),
    )
    actions = ["export_as_csv", "generate_table"]

    def generate_table(Student, request, queryset):
        """
        Generate action available in the admin page
        """
        for obj in queryset:
            Unregistered_instance = UnregisteredStudent(email=obj.email)
            Unregistered_instance.save()

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = StudentResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Student.csv"'
        return response

    export_as_csv.short_description = "Export Student details to CSV"


@admin.register(Scan)
class about_Admin(admin.ModelAdmin):
    model = Scan
    search_fields = ("student_id", "date")
    list_filter = ("date",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "student_id",
                    "date",
                    "breakfast",
                    "lunch",
                    "high_tea",
                    "dinner",
                ),
                #                "description": "%s" %_DESC_TEXT,
            },
        ),
    )


@admin.register(LongRebate)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LongRebateResource
    model = LongRebate
    autocomplete_fields = ["email"]
    search_fields = (
        "email__email",
        "approved",
        "date_applied",
    )
    list_filter = ("approved", "date_applied", "days")
    list_display = (
        "email",
        "date_applied",
        "approved",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    # "date_applied",
                    "start_date",
                    "end_date",
                    "days",
                    "approved",
                    "file",
                    "reason",
                ),
                "description": "%s" % REBATE_DESC_TEXT,
            },
        ),
    )
    actions = [
        "export_as_csv",
        "disapprove",
        "approve",
        "send_mail",
        "clean",
        "get_rebate_days_per_caterer",
        "get_spring_2025_days_per_caterer",
    ]

    @admin.action(description="Disapprove the students")
    def disapprove(self, request, queryset):
        """
        Disapprove action available in the admin page
        """
        for obj in queryset:
            obj.approved = False
            obj.save()

    @admin.action(description="Approve the students")
    def approve(self, request, queryset):
        """
        Approve action available in the admin page
        """
        for obj in queryset:
            obj.approved = True
            obj.save()

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = LongRebateResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="LongRebate.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"

    @admin.action(description="Send query mail to the students")
    def send_mail(self, request, queryset):
        """
        Send mail action available in the admin page
        """
        for obj in queryset:
            long_rebate_query_mail(obj.start_date, obj.end_date, obj.email.email)

    @admin.action(description="Get total rebate days per caterer for Autumn 2024")
    def get_rebate_days_per_caterer(self, request, queryset: list[LongRebate]):
        longRebates = []
        for obj in queryset:
            if obj.approved:
                longRebates.append(obj)
        return map_periods_to_long_rebate(longRebates, request.user)

    @admin.action(description="Get total rebate days per caterer for Spring 2025")
    def get_spring_2025_days_per_caterer(self, request, queryset: list[LongRebate]):
        longRebates = []
        for obj in queryset:
            if obj.approved:
                longRebates.append(obj)
        return map_periods_to_long_rebate(longRebates, request.user, "Spring 2025")


@admin.register(Rebate)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RebateResource
    model = Rebate
    autocomplete_fields = ["email"]
    search_fields = (
        "allocation_id__student_id",
        "approved",
        "date_applied",
        "start_date",
        "end_date",
        "email__email",
        "email__name",
    )
    list_filter = (
        "approved",
        "date_applied",
        "start_date",
        "end_date",
        "allocation_id__period",
    )
    list_display = (
        "date_applied",
        "email",
        "name",
        "start_date",
        "end_date",
        "approved",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "allocation_id",
                    "date_applied",
                    "start_date",
                    "end_date",
                    "approved",
                ),
                "description": "%s" % REBATE_DESC_TEXT,
            },
        ),
    )

    def get_queryset(self, request: HttpRequest):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.groups.filter(name="College Administration"):
            return qs
        return qs.filter(approved=True).filter(
            allocation_id__caterer__name=request.user.username
        )

    @admin.display(description="name")
    def name(self, obj):
        return getattr(obj.email, "name", None)

    actions = [
        "export_as_csv",
        "disapprove",
        "approve",
        "export_rebate_total",
        "find_overlapping_records",
        "check_negative_days",
    ]

    @admin.action(description="Disapprove the students")
    def disapprove(self, request, queryset):
        """
        Disapprove action available in the admin page
        """
        for obj in queryset:
            obj.approved = False
            obj.save()

    @admin.action(description="Approve the students")
    def approve(self, request, queryset):
        """
        Approve action available in the admin page
        """
        for obj in queryset:
            obj.approved = True
            obj.save()

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Rebate.csv"'
        return response

    def export_rebate_total(modeladmin, request, queryset):
        total_days = 0
        for obj in queryset:
            if obj.start_date > obj.end_date:
                continue
            total_days += (obj.end_date - obj.start_date).days + 1

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Rebate.csv"'

        writer = csv.writer(response)
        writer.writerow(["Total Days"])
        writer.writerow([total_days])

        return response

    def find_overlapping_records(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Rebate.csv"'

        writer = csv.writer(response)
        for obj in queryset:
            if obj.start_date > obj.end_date:
                obj.delete()
            rebates = (
                Rebate.objects.filter(email=obj.email)
                .filter(start_date__lte=obj.end_date)
                .filter(end_date__gte=obj.start_date)
                .exclude(pk=obj.pk)
            )
            for rebate in rebates:
                writer.writerow(
                    [
                        rebate.email,
                        rebate.start_date,
                        rebate.end_date,
                        getattr(rebate.email, "name", None),
                    ]
                )

        return response

    def check_negative_days(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Rebate.csv"'

        writer = csv.writer(response)
        for obj in queryset:
            if (obj.end_date - obj.start_date).days < 0:
                writer.writerow(
                    [
                        obj.email,
                        obj.start_date,
                        obj.end_date,
                        getattr(obj.email, "name", None),
                    ]
                )

        return response

    export_as_csv.short_description = "Export Rebate details to CSV"


def unregister_student(obj):
    for caterer in Caterer.objects.all():
        if caterer.student_limit > 0:
            available_caterer = caterer
            break
    student = Student.objects.filter(email__iexact=obj.email).last()
    high_tea = False
    period = obj.period
    student_id = str(available_caterer.name[0])
    student_id += "NH"
    available_caterer.student_limit -= 1
    student_id += str(available_caterer.student_limit)
    available_caterer.save(update_fields=["student_limit"])
    a = Allocation(
        email=student,
        student_id=student_id,
        period=period,
        caterer=caterer,
        high_tea=high_tea,
        jain=False,
        first_pref=caterer,
        second_pref=caterer,
        third_pref=caterer,
    )
    a.save()
    UnregisteredStudent.objects.filter(email=student.email).delete()


@admin.register(UnregisteredStudent)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UnregisteredStudentResource
    model = UnregisteredStudent
    search_fields = ("email",)
    list_filter = ("email",)
    list_display = ("email", "period")
    fieldsets = (
        (
            None,
            {
                "fields": ("email", "period"),
            },
        ),
    )

    actions = ["allocate", "check_student"]

    def set_period_action(semester_name, period_sno):
        @admin.action(
            description=f"Add Period as Semester: {semester_name} Period No.: {period_sno}"
        )
        def set_period(modeladmin, request, queryset):
            queryset.update(
                period=Period.objects.get(
                    semester=Semester.objects.get(name=semester_name), Sno=period_sno
                )
            )

        set_period.__name__ = f"set_period_{semester_name}_{period_sno}"
        return set_period

    try:
        for period in Period.objects.all():
            actions.append(set_period_action(period.semester.name, period.Sno))
    except Exception as e:
        print("Periods table not available", e)

    @admin.action(description="Allocate the unregistered students")
    def allocate(self, request, queryset):
        """
        Allocate action available in the admin page
        """
        for obj in queryset:
            print(obj.email)
            student = Student.objects.filter(email__iexact=obj.email).last()
            allocation = Allocation.objects.filter(
                email=student, period=obj.period
            ).exists()
            if allocation:
                print("deleted")
                UnregisteredStudent.objects.filter(email=obj.email).delete()
                continue
            unregister_student(obj)

    @admin.action(description="Check the students")
    def check_student(self, request, queryset):
        for obj in queryset:
            student = Student.objects.filter(email__iexact=obj.email).last()
            if student is None:
                print(obj.email)
                continue


rebate_fields = {
    "fields": (
        "email",
        (
            "period1_short",
            "period1_long",
            "period1_high_tea",
        ),
        "period1_bill",
        (
            "period2_short",
            "period2_long",
            "period2_high_tea",
        ),
        "period2_bill",
        (
            "period3_short",
            "period3_long",
            "period3_high_tea",
        ),
        "period3_bill",
        (
            "period4_short",
            "period4_long",
            "period4_high_tea",
        ),
        "period4_bill",
        (
            "period5_short",
            "period5_long",
            "period5_high_tea",
        ),
        "period5_bill",
        (
            "period6_short",
            "period6_long",
            "period6_high_tea",
        ),
        "period6_bill",
    ),
    "description": "%s" % REBATE_BILLS_DESC_TEXT,
}


@admin.register(StudentBills)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StudentBillsResource
    model = StudentBills
    search_fields = (
        "email__email",
        "email__hostel",
        "email__department",
        "email__degree",
        "email__roll_no",
        "email__name",
    )
    list_filter = ("semester", "email__hostel", "email__department", "email__degree")
    list_display = ("__str__", "semester", "roll_number", "name", "hostel")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "semester",
                    (
                        "period1_short",
                        "period1_long",
                        "period1_high_tea",
                    ),
                    "period1_bill",
                    (
                        "period2_short",
                        "period2_long",
                        "period2_high_tea",
                    ),
                    "period2_bill",
                    (
                        "period3_short",
                        "period3_long",
                        "period3_high_tea",
                    ),
                    "period3_bill",
                    (
                        "period4_short",
                        "period4_long",
                        "period4_high_tea",
                    ),
                    "period4_bill",
                    (
                        "period5_short",
                        "period5_long",
                        "period5_high_tea",
                    ),
                    "period5_bill",
                    (
                        "period6_short",
                        "period6_long",
                        "period6_high_tea",
                    ),
                    "period6_bill",
                ),
                "description": "%s" % REBATE_BILLS_DESC_TEXT,
            },
        ),
    )

    @admin.display(description="roll number")
    def roll_number(self, obj):
        return obj.email.roll_no if obj.email else ""

    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name if obj.email else ""

    @admin.display(description="hostel")
    def hostel(self, obj):
        return obj.email.hostel if obj.email else ""

    @admin.display(description="room number")
    def room_number(self, obj):
        return obj.email.room_no if obj.email else ""

    actions = ["export_as_csv", "update_bill", "fix_all_bills"]

    @admin.action(description="Update the bills")
    def update_bill(self, request, queryset):
        """
        Update action available in the admin page
        """
        for obj in queryset:
            days = obj.period6_short + obj.period6_long
            if obj.semester == Semester.objects.get(name="Autumn 2023"):
                days = 25 - days
                if obj.period6_high_tea:
                    obj.period6_bill = days * 130
                else:
                    obj.period6_bill = days * 115
                obj.save()

    @admin.action(description="Fix the bills")
    def fix_all_bills(self, request, queryset):
        for obj in queryset:
            if obj.semester != Semester.objects.get(name="Autumn 2024"):
                continue
            semester = obj.semester
            period_1 = Period.objects.get(semester=semester, Sno=1)
            period_2 = Period.objects.get(semester=semester, Sno=2)
            period_3 = Period.objects.get(semester=semester, Sno=3)
            fix_all_bills(obj, period_1, period_2, period_3)

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = StudentBillsResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="RebateAutumn.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"


@admin.register(Allocation)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_per_page = 500
    resource_class = AllocationResource
    model = Allocation
    autocomplete_fields = ["email"]
    search_fields = (
        "email__name",
        "email__roll_no",
        "email__hostel",
        "email__email",
        "student_id",
        "caterer__name",
    )
    list_filter = (
        "period",
        "caterer",
        "jain",
        "email__hostel",
        "email__degree",
        "email__department",
    )
    list_display = (
        "student_id",
        "name",
        "email",
        "period",
        "caterer",
        "jain",
        "registration_time",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "period",
                    "student_id",
                    "caterer",
                    # "high_tea",
                    "jain",
                    "first_pref",
                    "second_pref",
                    "third_pref",
                    "registration_time",
                ),
                "description": "%s" % ALLOCATION_DESC_TEXT,
            },
        ),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        semester = Semester.objects.first()
        if request.user.groups.filter(name="College Administration"):
            return qs
        return (
            qs.filter(period__semester=semester)
            .filter(
                period__Sno__in=[
                    1,
                ]
            )
            .filter(caterer__name=request.user.username)
        )

    @admin.display(description="email")
    def email(self, obj):
        return obj.email.email if obj.email else ""

    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name if obj.email else ""

    actions = ["export_as_csv", "fix_duplicates", "shift_caterer"]

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = AllocationResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="allocation.csv"'
        return response

    def fix_duplicates(self, request, queryset):
        emails = []
        for obj in queryset:
            emails.append(obj.email.email)
        for obj in queryset:
            period = Period.objects.get(
                Sno=3, semester=Semester.objects.get(name="Spring 2025")
            )
            allocations = Allocation.objects.filter(
                email__email=obj.email.email, period=period
            )
            if len(allocations) > 1:
                for allocation in allocations[1:]:
                    allocation.delete()

    def shift_caterer(self, request, queryset):
        caterers = Caterer.objects.all()
        student_limit = {}

        for caterer in caterers:
            period = Period.objects.get(
                Sno=3, semester=Semester.objects.get(name="Spring 2025")
            )
            allocations = Allocation.objects.filter(
                caterer=caterer, period=period
            ).order_by("registration_time")
            student_limit[caterer.name] = [
                caterer.student_limit - len(allocations),
                allocations,
            ]

        for caterer in caterers:
            limit = caterer.student_limit
            count = student_limit[caterer.name][0]
            allocations = student_limit[caterer.name][1]
            if count < 0:
                for allocation in allocations[limit:]:
                    second_pref = allocation.second_pref
                    if student_limit[second_pref][0] > 0:
                        allocation.caterer = Caterer.objects.get(name=second_pref)
                        allocation.save()
                        student_limit[second_pref][0] -= 1
                    else:
                        third_pref = allocation.third_pref
                        if student_limit[third_pref][0] > 0:
                            allocation.caterer = Caterer.objects.get(name=third_pref)
                            allocation.save()
                            student_limit[third_pref][0] -= 1

    export_as_csv.short_description = "Export Allocation details to CSV"


@admin.register(Period)
class about_Admin(admin.ModelAdmin):
    list_display = ("Sno", "start_date", "end_date", "semester")
    model = Period
    fieldsets = (
        (
            None,
            {"fields": ("Sno", "start_date", "end_date", "semester")},
        ),
    )


caterer_bill_fields = {
    "fields": (
        "caterer",
        "period1_bills",
        "period2_bills",
        "period3_bills",
        "period4_bills",
        "period5_bills",
        "period6_bills",
    ),
    # "description": "%s" % CATERER_BILL_DESC_TEXT,
}


@admin.register(CatererBills)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CatererBillsResource
    model = CatererBills
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "caterer",
                    "semester",
                    "period1_bills",
                    "period2_bills",
                    "period3_bills",
                    "period4_bills",
                    "period5_bills",
                    "period6_bills",
                ),
                # "description": "%s" % CATERER_BILL_DESC_TEXT,
            },
        ),
    )
    list_display = (
        "__str__",
        "semester",
        "period1_bills",
        "period2_bills",
        "period3_bills",
        "period4_bills",
        "period5_bills",
        "period6_bills",
    )
    search_fields = ("caterer__name",)
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = CatererBillsResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="caterer_bills.csv"'
        return response

    export_as_csv.short_description = "Export Caterer Bills details to CSV"


@admin.register(LeftLongRebate)
class about_Admin(admin.ModelAdmin):
    model = LeftLongRebate
    search_fields = ("email",)
    list_display = ("email", "start_date", "end_date")
    fieldsets = (
        (
            None,
            {"fields": ("email", "start_date", "end_date")},
        ),
    )

    actions = ["Add"]

    @admin.action(description="Add left long rebate to Bills")
    def Add(self, request, queryset):
        """
        Export action available in the admin page
        """
        for obj in queryset:
            email = obj.email
            student = Student.objects.filter(email=email).last()
            days_per_period = fill_periods(student, obj.start_date, obj.end_date)
            save_long_bill(student, days_per_period, 1)


@admin.register(LeftShortRebate)
class about_Admin(admin.ModelAdmin):
    model = LeftShortRebate
    search_fields = ("email",)
    list_display = ("email", "start_date", "end_date")
    fieldsets = (
        (
            None,
            {"fields": ("email", "start_date", "end_date", "date_applied")},
        ),
    )

    actions = ["Add"]

    @admin.action(description="Add left short rebate to Bills")
    def Add(self, request, queryset: list[LeftShortRebate]):
        """
        Export action available in the admin page
        """
        for obj in queryset:
            email = obj.email
            student_obj = Student.objects.filter(email=email).last()
            for period in Period.objects.all():
                if period.start_date <= obj.start_date <= period.end_date:
                    start_date = obj.start_date
                    end_date = obj.end_date
                    date_applied = obj.date_applied
                    if period.end_date < obj.end_date:
                        obj.start_date = period.end_date + timedelta(days=1)
                        obj.save()
                        end_date = period.end_date
                    else:
                        obj.delete()
                    allocation = Allocation.objects.filter(
                        email=student_obj, period=period
                    ).last()
                    if allocation:
                        upper_cap_check = max_days_rebate(
                            student_obj, start_date, end_date, period
                        )
                        if upper_cap_check > 0:
                            end_date = start_date + timedelta(
                                days=(upper_cap_check - 1)
                            )
                        short_rebate = Rebate(
                            email=student_obj,
                            allocation_id=allocation,
                            start_date=start_date,
                            end_date=end_date,
                            date_applied=date_applied,
                            approved=True,
                        )
                        short_rebate.save()


@admin.register(AllocationForm)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = AllocationFormResource
    model = AllocationForm
    search_fields = ("start_time", "end_time", "heading", "period__Sno")
    list_filter = ("start_time", "end_time", "heading", "period__Sno")
    list_display = ("__str__", "start_time", "end_time", "active", "period")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "heading",
                    "description",
                    "period",
                    "start_time",
                    "end_time",
                    "active",
                    "show_allocated",
                )
            },
        ),
    )


@admin.register(Semester)
class about_admin(admin.ModelAdmin):
    model = Semester
    search_fields = ("name",)
    list_display = ("name",)
    fieldsets = (
        (
            None,
            {"fields": ("name",)},
        ),
    )


@admin.register(Fee)
class about_Admin(admin.ModelAdmin):
    model = Fee
    search_fields = ("program",)
    list_display = ("program", "prev_sem_fee", "upcoming_sem_fee")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "program",
                    "prev_sem_fee",
                    "upcoming_sem_fee",
                )
            },
        ),
    )
