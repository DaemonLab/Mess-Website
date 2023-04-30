import re
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip("/"))]
if hasattr(settings, "LOGIN_EXEMPT_URLS"):
    EXEMPT_URLS += [re.compile(url.lstrip("/")) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware Called")
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
            '''
            To check if the user is authenticated, If not redirect it to the google login page
            '''
            if (request.path =="/rebateForm/"):
                print(request.path)
                settings.LOGIN_REDIRECT_URL = request.path
                return redirect(settings.LOGIN_URL+ "?next=" + request.path)
            if (request.path =="/allocation/"):
                print(request.path)
                settings.LOGIN_REDIRECT_URL = request.path
                return redirect(settings.LOGIN_URL+ "?next=" + request.path)
            if (request.path =="/addAllocation/"):
                print(request.path)
                settings.LOGIN_REDIRECT_URL = request.path
                return redirect(settings.LOGIN_URL+ "?next=" + request.path)
