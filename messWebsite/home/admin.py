from django.contrib import admin
from home.models import About, Update, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact

# Register your models here.

admin.site.register((About, Update, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact))
