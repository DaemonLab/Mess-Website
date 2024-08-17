from django.apps import AppConfig

"""
File-name: apps.py
Register your apps here
Class: HomeConfig
"""


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        import socket

        # bind to port 47200, then check for it for every worker
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("127.0.0.1", 47200))
        except socket.error:
            print, "!!!scheduler already started, DO NOTHING"
        else:
            from .schedulers import start

            start()
