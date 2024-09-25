from django.contrib import admin
from .models import MessCard

class MessCardAdmin(admin.ModelAdmin):
    list_display = ['allocation', 'student']
    search_fields = ('allocation__student_id', 'allocation__email__email')
    list_filter = ('allocation__caterer__name',)
    raw_id_fields = ('allocation', 'student')

admin.site.register(MessCard, MessCardAdmin)
