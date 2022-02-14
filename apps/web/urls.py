from apps.web.views import HomeView, receive_contact_information
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view()),
    path('contact/', receive_contact_information)
]