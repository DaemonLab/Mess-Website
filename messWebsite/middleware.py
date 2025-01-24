import re

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip("/"))]
if hasattr(settings, "LOGIN_EXEMPT_URLS"):
    EXEMPT_URLS += [re.compile(url.lstrip("/")) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, "user")
        path = request.path_info.lstrip("/")
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse("account_logout").lstrip("/"):
            logout(request)
            return

        if (not request.user.is_authenticated) and (not url_is_exempt):
            """
            To check if the user is authenticated, If not redirect it to the google login page
            """
            if request.path == "/rebateForm/":
                return redirect(settings.LOGIN_URL + "?next=" + request.path)
            if request.path == "/allocation/":
                return redirect(settings.LOGIN_URL + "?next=" + request.path)
            if request.path == "/addAllocation/":
                return redirect(settings.LOGIN_URL + "?next=" + request.path)
            if request.path == "/longRebate/":
                return redirect(settings.LOGIN_URL + "?next=" + request.path)
