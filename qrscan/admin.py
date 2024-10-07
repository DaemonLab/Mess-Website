from django.contrib import admin
from .models import MessCard, Meal, MessTiming

# Admin configuration for MessCard model
@admin.register(MessCard)
class MessCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'allocation', 'student']
    list_display_links = ['id', 'allocation', 'student']
    search_fields = ('allocation__student_id', 'allocation__email__email')
    list_filter = ('allocation__caterer__name',)
    raw_id_fields = ('allocation', 'student')
    ordering = ['id']
    list_per_page = 25


# Admin configuration for Meal model
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'mess_card', 'date', 'breakfast', 'lunch', 'dinner']
    list_display_links = ['id', 'mess_card']
    search_fields = ('mess_card__allocation__student_id', 'mess_card__allocation__email__email')
    list_filter = ('mess_card__allocation__caterer__name', 'date', 'breakfast', 'lunch', 'dinner')
    raw_id_fields = ('mess_card',)
    ordering = ['date', 'id']
    list_per_page = 25


# Admin configuration for MessTimings model
@admin.register(MessTiming)
class MessTimingsAdmin(admin.ModelAdmin):
    list_display = ['meal_type', 'start_time', 'end_time']
    list_display_links = ['meal_type']
    search_fields = ('meal_type',)
    list_filter = ('meal_type',)
    ordering = ['meal_type']

    def start_time(self, obj):
        return obj.start_time.strftime('%H:%M')
    
    def end_time(self, obj):
        return obj.end_time.strftime('%H:%M')
