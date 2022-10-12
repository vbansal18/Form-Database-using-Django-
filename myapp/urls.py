from django.contrib import admin
from django.urls import path, include
from myapp import views


urlpatterns = [
    path("", views.index, name = 'home'),
    path("Contact", views.contact, name = 'Contact'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
]
