from django.urls import path
from football import views

urlpatterns = [
    path("", views.home, name="home"),
]