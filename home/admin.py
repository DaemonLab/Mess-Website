"""
File-name: admin.py
This file is registers the models on the adming page and customizes the admin page
For more information please see: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
"""
from django.contrib import admin
from django.http import HttpResponse
import datetime
from django.utils.translation import gettext_lazy as _
from .utils.django_email_server import rebate_mail,caterer_mail, long_rebate_query_mail
from .utils.rebate_bills_saver import save_short_bill, save_long_bill, update_bills
from .utils.month import fill_periods
from home.models import (
    About,
    Update,
    Rule,
    Carousel,
    ShortRebate,
    Caterer,
    Form,
    Cafeteria,
    Contact,
    Student,
    Scan,
    Rebate,
    LongRebate,
    UnregisteredStudent,
    TodayRebate,
    AllocationAutumn22,
    AllocationSpring23,
    RebateAutumn22,
    RebateSpring23,
    CatererBillsAutumn22,
    CatererBillsSpring23,
    PeriodAutumn22,
    PeriodSpring23,
    LeftLongRebate,
    LeftShortRebate,
    AllocationForm,
    Period,
    Semester,
    StudentBills,
    CatererBills,
    Allocation,
    Fee,
)
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from .resources import (
    StudentResource,
    # AllocationResource,
    RebateResource,
    RebateBillsResource,
    UnregisteredStudentResource,
    LongRebateResource,
    # CatererBillsResource,
    StudentBillsResource,
    CatererBillsNewResource,
    AllocationNewResource,
)

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
REBATE_DESC_TEXT = "This contains the rebate details of each rebate applied by the students."
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
class about_Admin(admin.ModelAdmin):
    model = Caterer
    search_fields = ("name",)
    list_filter = ("id","name",)
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
    def generate_table(self,request,queryset):
        semester = Semester.objects.filter().last()
        for caterer in queryset:
            caterer_bill,_ = CatererBills.objects.get_or_create(caterer=caterer,semester=semester)
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
    search_fields = ("name", "roll_no", "hostel", "degree", "department")
    list_display = ("name", "roll_no", "hostel", "email")
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
    autocomplete_fields = ['email']
    search_fields = ("email__email","approved", "date_applied", )
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
                ),
                "description": "%s" % REBATE_DESC_TEXT,
            },
        ),
    )
    actions = ["export_as_csv", "disapprove", "approve","send_mail","clean"]

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

    # @admin.action(description="Clean left long rebate data")
    # def clean(self, request, queryset):
    #     """
    #     Clean left long rebate data
    #     """
    #     for obj in queryset:
    #         if(obj.approved==True):
    #             if(obj.end_date>datetime.date(2023,12,7)):
    #                 print(obj.end_date)
    #                 obj.approved=False
    #                 obj.save()
    #                 print(obj.approved)
    #                 obj.approved=True
    #                 obj.save()

@admin.register(Rebate)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RebateResource
    model = Rebate
    search_fields = (
        "allocation_id__student_id",
        "approved",
        "date_applied",
        "start_date",
        "end_date",
        "email__email",
    )
    list_filter = ("approved", "date_applied", "start_date", "end_date")
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
    
    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name
    
    actions = ["export_as_csv", "disapprove", "approve"]

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

    export_as_csv.short_description = "Export Rebate details to CSV"

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     update_bill(instance=obj, sender=obj.__class__, created=change)

    # def save_related(self, request, form, formsets, change):
    #     super().save_related(request, form, formsets, change)
    #     print("save related")
    #     update_bill(
    #         sender=form.instance.__class__, instance=form.instance, created=change
    #     )

def unregister_student(obj):
    for caterer in Caterer.objects.all():
        if caterer.student_limit > 0:
            available_caterer=caterer
            break
    student= Student.objects.filter(email=obj.email).last()
    high_tea=False
    period = obj.period
    student_id = str(available_caterer.name[0])
    student_id += "NH"
    student_id += str(available_caterer.student_limit)
    available_caterer.student_limit -= 1
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
    list_display = ("email","period")
    fieldsets = (
        (
            None,
            {
                "fields": ("email","period"),
            },
        ),
    )
    
    actions = ["allocate",]

    def set_period_action(semester_name, period_sno):
        @admin.action(description=f'Add Period as Semester: {semester_name} Period No.: {period_sno}')
        def set_period(modeladmin, request, queryset):
            queryset.update(period=Period.objects.get(semester=Semester.objects.get(name=semester_name), Sno=period_sno))
        set_period.__name__ = f'set_period_{semester_name}_{period_sno}'
        return set_period
    
    for period in Period.objects.all():
        actions.append(set_period_action(period.semester.name, period.Sno))


    @admin.action(description="Allocate the unregistered students")
    def allocate(self, request, queryset):
        """
        Allocate action available in the admin page
        """
        for obj in queryset:
            unregister_student(obj)

@admin.register(TodayRebate)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    model = TodayRebate
    search_fields = ("Caterer","allocation_id","date")
    list_display =("allocation_id", "date","start_date","end_date")
    # list_filter = ()
    fieldsets = (  
        (
            None,
            {
                "fields": (
                    "date",
                    "Caterer",
                    "allocation_id",
                    "start_date",
                    "end_date",
                )
            },
        ),
    )

    actions = ["send_mail"]

    @admin.action(description="Send mail to the caterer")
    def send_mail(self, request, queryset):
        text = "<li> {name} with {allocation_id} has applied from {start_date} to {end_date}</li>"
        for caterer in Caterer.objects.all():
            print(caterer.name)
            message_caterer = ""
            for obj in queryset:
                print(obj.Caterer)
                if(obj.Caterer != caterer.name): continue
                allocation=obj.allocation_id
                message_caterer +=(text.format(allocation_id=allocation.student_id,name=allocation.email.name, start_date=obj.start_date, end_date=obj.end_date))
                obj.delete()
            print(message_caterer)
            if(message_caterer): caterer_mail(message_caterer, caterer.name,caterer.email, obj.date)
        

rebate_fields={"fields": (
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

@admin.register(RebateAutumn22)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    model=RebateAutumn22
    resource_class = RebateBillsResource
    search_fields = ("email__email","email__hostel","email__department","email__degree","email__roll_no","email__name")
    list_filter = ("email__hostel","email__department","email__degree")
    list_display = ("__str__","roll_number","name","hostel")
    fieldsets = ((None,rebate_fields,),)

    @admin.display(description="roll number")
    def roll_number(self, obj):
        return obj.email.roll_no
    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name
    @admin.display(description="hostel")
    def hostel(self, obj):
        return obj.email.hostel
    @admin.display(description="room number")
    def room_number(self, obj):
        return obj.email.room_no

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateBillsResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="RebateAutumn.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"

@admin.register(RebateSpring23)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RebateBillsResource
    model=RebateSpring23
    search_fields = ("email__email","email__hostel","email__department","email__degree","email__roll_no","email__name")
    list_filter = ("email__hostel","email__degree","email__department")
    list_display = ("__str__","roll_number","name","hostel")
    fieldsets = ((None,rebate_fields,),)

    @admin.display(description="roll number")
    def roll_number(self, obj):
        return obj.email.roll_no
    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name
    @admin.display(description="hostel")
    def hostel(self, obj):
        return obj.email.hostel
    @admin.display(description="room number")
    def room_number(self, obj):
        return obj.email.room_no

    actions = ["export_as_csv","clean"]

    @admin.action(description="Clean Null period data")
    def clean(self, request, queryset):
        """
        Clean testing period data
        """
        for obj in queryset:
            if(obj.period1_short==None):
                obj.period1_short = 0
            if(obj.period1_long==None):
                obj.period1_long = 0
            if(obj.period2_short==None):
                obj.period2_short = 0
            if(obj.period2_long==None):
                obj.period2_long = 0
            if(obj.period3_short==None):
                obj.period3_short = 0
            if(obj.period3_long==None):
                obj.period3_long = 0
            if(obj.period4_short==None):
                obj.period4_short = 0
            if(obj.period4_long==None):
                obj.period4_long = 0
            if(obj.period5_short==None):
                obj.period5_short = 0
            if(obj.period5_long==None):
                obj.period5_long = 0
            if(obj.period6_short==None):
                obj.period6_short = 0
            if(obj.period6_long==None):
                obj.period6_long = 0
            if(obj.period1_high_tea==None):
                obj.period1_high_tea = True
            if(obj.period2_high_tea==None):
                obj.period2_high_tea = True
            if(obj.period3_high_tea==None):
                obj.period3_high_tea = True
            if(obj.period4_high_tea==None):
                obj.period4_high_tea = True
            if(obj.period5_high_tea==None):
                obj.period5_high_tea = True
            if(obj.period6_high_tea==None):
                obj.period6_high_tea = True
            if(obj.period1_bill==None):
                obj.period1_bill = 0
            if(obj.period2_bill==None):
                obj.period2_bill = 0
            if(obj.period3_bill==None):
                obj.period3_bill = 0
            if(obj.period4_bill==None):
                obj.period4_bill = 0
            if(obj.period5_bill==None):
                obj.period5_bill = 0
            if(obj.period6_bill==None):
                obj.period6_bill = 0
            obj.save()

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateBillsResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="RebateAutumn.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"

@admin.register(StudentBills)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StudentBillsResource
    model=StudentBills
    search_fields = ("email__email","email__hostel","email__department","email__degree","email__roll_no","email__name")
    list_filter = ("email__hostel","email__department","email__degree")
    list_display = ("__str__","roll_number","name","hostel")
    fieldsets = ((None,
                  {"fields": (
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
                   }        
                ,),)

    @admin.display(description="roll number")
    def roll_number(self, obj):
        return obj.email.roll_no
    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name
    @admin.display(description="hostel")
    def hostel(self, obj):
        return obj.email.hostel
    @admin.display(description="room number")
    def room_number(self, obj):
        return obj.email.room_no

    actions = ["export_as_csv", "update_bill"]

    @admin.action(description="Update the bills")
    def update_bill(self, request, queryset):
        """
        Update action available in the admin page
        """
        for obj in queryset:
            days = obj.period4_short + obj.period4_long
            if(obj.period4_high_tea):
                continue
            days = 31 - days
            obj.period4_bill = days * 115
            obj.save()
    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = RebateBillsResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="RebateAutumn.csv"'
        return response

    export_as_csv.short_description = "Export Rebate details to CSV"


@admin.register(Allocation)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AllocationNewResource
    model = Allocation
    search_fields = ("email__name","email__roll_no","email__hostel","email__email","student_id", "caterer__name", "high_tea",)
    list_filter = ("period", "caterer", "high_tea","jain","email__hostel","email__degree","email__department",)
    list_display = ("student_id","name","email","period", "caterer", "high_tea","jain")
    fieldsets = ((None,
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
                    ),
                    "description": "%s" % ALLOCATION_DESC_TEXT,
                  }
                ,),)

    @admin.display(description="email")
    def email(self, obj):
        return obj.email.email
    
    @admin.display(description="name")
    def name(self, obj):
        return obj.email.name

    
    actions = ["export_as_csv","correct_bills", "correct_bills4"]

    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = AllocationNewResource()
        dataset = resource.export(queryset)
        response = HttpResponse(dataset.csv, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="allocation.csv"'
        return response
    

    def correct_bills(self,request,queryset):
        for obj in queryset:
                if(obj.period==Period.objects.get(Sno=5, semester=Semester.objects.get(name="Autumn 2023"))):
                    update_bills(obj.email,obj)
                    obj.save()
                if(obj.period==Period.objects.get(Sno=4, semester=Semester.objects.get(name="Autumn 2023"))):
                    update_bills(obj.email,obj)
                    obj.save()
    

    export_as_csv.short_description = "Export Allocation details to CSV"


   
@admin.register(Period)
class about_Admin(admin.ModelAdmin):
    list_display = ("Sno", "start_date", "end_date", "semester")
    model = Period
    fieldsets = (
        (None,{"fields": ("Sno", "start_date", "end_date","semester")},),)
    
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


# @admin.register(CatererBillsSpring23)
# class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
#     resource_class = CatererBillsResource
#     model = CatererBillsSpring23
#     fieldsets = ((None,caterer_bill_fields,),)
#     list_display = ("__str__", "period1_bills", "period2_bills", "period3_bills", "period4_bills", "period5_bills", "period6_bills",)
#     search_fields = ("caterer__name",)
#     actions = ["export_as_csv"]
    
#     def export_as_csv(self, request, queryset):
#         """
#         Export action available in the admin page
#         """
#         resource = CatererBillsResource()
#         dataset = resource.export(queryset)
#         response = HttpResponse(dataset.csv, content_type="text/csv")
#         response["Content-Disposition"] = 'attachment; filename="caterer_bills.csv"'
#         return response
    
#     export_as_csv.short_description = "Export Caterer Bills details to CSV"

@admin.register(CatererBills)
class about_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CatererBillsNewResource
    model = CatererBills
    fieldsets = ((None,
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
            }
                  ,),)
    list_display = ("__str__", "semester","period1_bills", "period2_bills", "period3_bills", "period4_bills", "period5_bills", "period6_bills",)
    search_fields = ("caterer__name",)
    actions = ["export_as_csv"]
    
    def export_as_csv(self, request, queryset):
        """
        Export action available in the admin page
        """
        resource = CatererBillsNewResource()
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
        (None,{"fields": ("email", "start_date", "end_date")},),)
    
    actions = ["Add"]

    @admin.action(description="Add left long rebate to Bills")
    def Add(self, request, queryset):
        """
        Export action available in the admin page
        """
        for obj in queryset:
            email = obj.email
            student = Student.objects.filter(email=email).last()
            days_per_period = fill_periods(student,obj.start_date, obj.end_date)
            save_long_bill(student, days_per_period,1)

@admin.register(LeftShortRebate)
class about_Admin(admin.ModelAdmin):
    model = LeftShortRebate
    search_fields = ("email",)
    list_display = ("email", "start_date", "end_date")
    fieldsets = (
        (None,{"fields": ("email", "start_date", "end_date","date_applied")},),)
    
    actions = ["Add"]

    @admin.action(description="Add left short rebate to Bills")
    def Add(self, request, queryset):
        """
        Export action available in the admin page
        """
        for obj in queryset:
            email = obj.email
            student_obj = Student.objects.filter(email=email).last()
            for period in Period.objects.all():
                if(period.start_date <= obj.start_date and period.end_date >= obj.end_date):
                    days = (obj.end_date - obj.start_date).days + 1
                    allocation=Allocation.objects.filter(email=student_obj,period=period).last()
                    if allocation:
                        save_short_bill(student_obj,period,days,allocation.high_tea,allocation.caterer)
                        new_rebate = TodayRebate(date=obj.date_applied,Caterer=allocation.caterer,allocation_id = allocation,start_date=obj.start_date,end_date=obj.end_date)
                        new_rebate.save()
                        print("Saved")
                        short_rebate = Rebate(
                            email=student_obj,
                            allocation_id=allocation,
                            start_date=obj.start_date,
                            end_date=obj.end_date,
                            date_applied=obj.date_applied,
                            approved=True,
                        )
                        short_rebate.save()
                        LeftShortRebate.objects.filter(email=email, date_applied = obj.date_applied).delete()
                    

@admin.register(AllocationForm)
class about_Admin(ImportExportModelAdmin,admin.ModelAdmin):
    # resource_class = AllocationFormResource
    model = AllocationForm
    search_fields = ("start_time","end_time","heading","period__Sno")
    list_filter = ("start_time","end_time","heading","period__Sno")
    list_display = ("__str__", "start_time", "end_time","active")
    fieldsets = (
        (None,
            {"fields": 
                (
                    "heading", 
                    "description", 
                    "period",
                    "start_time",
                    "end_time",
                    "active",
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
        (None,{"fields": ("name",)},),)
    

@admin.register(Fee)
class about_Admin(admin.ModelAdmin):
    model = Fee
    search_fields = ("program",)
    list_display = ("program", "prev_sem_fee", "upcoming_sem_fee")
    fieldsets = (
        (None,
         {"fields": 
          (
            "program", 
            "prev_sem_fee",
            "upcoming_sem_fee",
           )
         },
        ),
    )
    