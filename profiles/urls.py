from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView
from .views import CustomPasswordChangeView

app_name = "profiles"

urlpatterns = [
    path("", views.profile, name="profile"),
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_change_password"),
    path(
        "password/change/done/",
        PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),
        name="password_change_done",
    ),
]