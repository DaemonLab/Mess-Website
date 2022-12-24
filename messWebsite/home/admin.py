from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from home.models import (
    About,
    Update,
    Rule,
    Penalty,
    ShortRebate,
    LongRebate,
    Caterer,
    Form,
    Cafeteria,
    Contact,
)

#Customising the heading and title of the admin page
admin.site.site_header = 'Dining Website Admin Page'
admin.site.site_title = 'Admin Page'
admin.site.index_title = 'Website Admin panel'



#Text of description content of each model
ABOUT_DESC_TEXT="This contains the content that will show up in the about section of the home page. Add all of the About us Content in one field itself."
UPDATE_DESC_TEXT="This contains the content that will show up in the update section of the home page. Add new field for each new update."
RULE_DESC_TEXT="This contains the content that will show up in the rule section of the Rules page. Add new field for each new rule."
PENALTY_DESC_TEXT="This contains the content that will show up in the penalty section of the Rules page. Add new field for each new penalty."
SHORT_REBATE_DESC_TEXT="This contains the content that will show up in the short rebate section of the rules page. Add all of the short term rebate Content in one field itself."
LONG_REBATE_DESC_TEXT="This contains the content that will show up in the rule section of the Rules page. Add new field for each new rule."
CATERER_DESC_TEXT="This contains the content that will show up in the respective caterers page. Add new field for each new caterer."
FORM_DESC_TEXT="This contains the content that will show up in the forms page. Add new field for each new form data."
CAFETERIA_DESC_TEXT="This contains the content that will show up in the cafeteria page. Add new field for each new cafeteria."
CONTACT_DESC_TEXT="This contains the content that will show up in the contact page. Add new field for each new contact."

# Register your models here
@admin.register(About)
class about_Admin(admin.ModelAdmin):
    model = About
#    ordering=("description",)
#    search_fields = ("description")
#    list_display = ("description")
#    list_filter = ("description",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "description",
                ),
                "description": "%s" %ABOUT_DESC_TEXT,
            },
        ),
    )

@admin.register(Update)
class about_Admin(admin.ModelAdmin):
    model = Update
    ordering = ("-time_stamp",)
    search_fields = ("update","time_stamp")
#    list_display = ("update","time_stamp")
    list_filter = ("time_stamp",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "update",
                ),
                "description": "%s" %UPDATE_DESC_TEXT,
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
                "fields": (
                    "rule",
                ),
                "description": "%s" %RULE_DESC_TEXT,
            },
        ),
    )

@admin.register(Penalty)
class about_Admin(admin.ModelAdmin):
    model = Penalty
    ordering = ("penalty",)
    search_fields = ("penalty",)
    list_display = ("penalty",)
    list_filter = ("penalty",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "penalty",
                ),
                "description": "%s" %PENALTY_DESC_TEXT,
            },
        ),
    )

@admin.register(ShortRebate)
class about_Admin(admin.ModelAdmin):
    model = ShortRebate
#    ordering = ("",)
#    search_fields = ("",)
#    list_display = ("",)
#    list_filter = ("",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "desc",
                    "link",
                    'policy',
                    'circulation',
                    'infoToCaterer',
                    'note',
                    'Memebers',
                    'biling',
                ),
                "description": "%s" %SHORT_REBATE_DESC_TEXT,
            },
        ),
    )

@admin.register(LongRebate)
class about_Admin(admin.ModelAdmin):
    model = LongRebate
    ordering = ("rule",)
    search_fields = ("rule",)
    list_display = ("rule",)
    list_filter = ("rule",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "rule",
                ),
                "description": "%s" %LONG_REBATE_DESC_TEXT,
            },
        ),
    )

@admin.register(Caterer)
class about_Admin(admin.ModelAdmin):
    model = Caterer
#    ordering = ("name",)
    search_fields = ("name",)
#    list_display = ()
    list_filter = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "upper_description",
                    "sheet_url",
                    "lower_description",
                ),
                "description": "%s" %CATERER_DESC_TEXT,
            },
        ),
    )

@admin.register(Form)
class about_Admin(admin.ModelAdmin):
    model = Form
#    ordering = ("name",)
    search_fields = ("heading","description")
#    list_display = ()
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
                "description": "%s" %FORM_DESC_TEXT,
            },
        ),
    )

@admin.register(Cafeteria)
class about_Admin(admin.ModelAdmin):
    model = Cafeteria
#    ordering = ()
    search_fields = ("name","poc")
#    list_display = ()
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
                "description": "%s" %CAFETERIA_DESC_TEXT,
            },
        ),
    )

@admin.register(Contact)
class about_Admin(admin.ModelAdmin):
    model = Contact
#    ordering = ("rule",)
    search_fields = ("occupation","name","hostel_sec")
#    list_display = ("rule",)
    list_filter = ("occupation","hostel_sec")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("occupation","hostel_sec"),
                    "name",
                    "contact",
                    "email",
                ),
                "description": "%s" %CONTACT_DESC_TEXT,
            },
        ),
    )
