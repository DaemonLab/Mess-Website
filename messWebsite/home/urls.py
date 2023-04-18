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
    # path("kanaka/", views.kanaka, name="kanaka"),
    # path("ajay/", views.ajay, name="ajay"),
    path("caterer/<str:name>", views.caterer, name="caterer"),
    path("links/", views.links, name="links"),
    path("cafeteria/", views.cafeteria, name="cafeteria"),
    path("contact/", views.contact, name="contact"),
    path("rebateForm/", views.rebate, name="rebate"),
    url('allocation/', allocation.as_view(), name='allocation'),
]