from django.apps import AppConfig
'''
File-name: apps.py
Functions: base
Register your apps here
'''

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"
