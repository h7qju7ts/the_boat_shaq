from django.urls import path
from .views import home
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "boats"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("catalog/<slug:category_slug>/", views.catalog, name="catalog_by_category"),
    path("boat/<slug:slug>/", views.boat_detail, name="boat_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
