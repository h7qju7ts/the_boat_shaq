from django.urls import path
from .views import home, profile
from . import views

app_name = "boats"

urlpatterns = [
    path("", home, name="home"),
    path("profile/", profile, name="profile"),
]
