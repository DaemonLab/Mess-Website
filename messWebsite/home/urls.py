from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("rules", views.rules, name="rules"),
    path("kanaka", views.kanaka, name="kanaka"),
    path("ajay", views.ajay, name="ajay"),
    path("links", views.links, name="links"),
    path("cafeteria", views.cafeteria, name="cafeteria"),
    path("contact", views.contact, name="contact"),
]