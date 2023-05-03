"""messWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:

    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')

    Class-based views

        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
        
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import logout
from allauth.socialaccount.providers.google.views import oauth2_login, oauth2_callback

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path("admin/", admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('accounts/logout/', logout, name="account_logout"),
    path('accounts/google/login/', oauth2_login, name="google_login"),
    path('accounts/google/login/callback/', oauth2_callback, name="google_callback"),
    path("", include('home.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
