from django.apps import AppConfig
'''
File-name: apps.py
Register your apps here
Class: HomeConfig
'''

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        import home.signals

