from django.urls import path
from .views import home, profile
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("accounts/profile/", profile, name="profile"),
]