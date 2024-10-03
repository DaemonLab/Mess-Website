from django.contrib import admin
from .models import MessCard, Meal

class MessCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'allocation', 'student']
    search_fields = ('allocation__student_id', 'allocation__email__email')
    list_filter = ('allocation__caterer__name',)
    raw_id_fields = ('allocation', 'student')


class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'mess_card', 'date', 'breakfast', 'lunch', 'dinner']
    search_fields = ('mess_card__allocation__student_id', 'mess_card__allocation__email__email')
    list_filter = ('mess_card__allocation__caterer__name', 'date', 'breakfast', 'lunch', 'dinner')
    raw_id_fields = ('mess_card',)


admin.site.register(MessCard, MessCardAdmin)
admin.site.register(Meal, MealAdmin)
