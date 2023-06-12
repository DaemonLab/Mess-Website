"""Mess Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:

    Function views (This is used here)
        1. Add an import:  from . import views
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
from . import views
from .views import *
from django.urls import re_path as url

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("rules/", views.rules, name="rules"),
    path("caterer/<str:name>", views.caterer, name="caterer"),
    path("links/", views.links, name="links"),
    path("cafeteria/", views.cafeteria, name="cafeteria"),
    path("contact/", views.contact, name="contact"),
    path("rebateForm/", views.rebate, name="rebate"),
    path('allocation/', views.allocation, name='allocation'),
    path('longRebate/', views.addLongRebateBill, name='addLongRebateBill'),
    path('profile/', views.profile, name='profile'),
    path('allocationForm/', views.allocationForm, name='allocationForm'),
    path('period_data/', views.period_data, name='period_data'),
    path('rebate_data/', views.rebate_data, name='rebate_data'),
]