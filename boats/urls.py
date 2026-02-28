from django.urls import path
from .views import home, profile
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "boats"

urlpatterns = [
    path("", home, name="home"),
    path("profile/", profile, name="profile"),
    path("", views.catalog, name="catalog"),
    path("<slug:slug>/", views.boat_detail, name="boat_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
