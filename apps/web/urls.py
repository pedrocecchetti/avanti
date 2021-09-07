from apps.web.views import HomeView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view()),
]