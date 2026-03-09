from django.urls import path
from . import views

app_name = "basket"

urlpatterns = [
    path("", views.view_basket, name="basket"),
    path("add/<int:boat_id>/", views.add_to_basket, name="add_to_basket"),
    path("decrease/<int:boat_id>/", views.decrease_basket, name="decrease_basket"),
    path("remove/<int:boat_id>/", views.remove_from_basket, name="remove_from_basket"),
    path("clear/", views.clear_basket, name="clear_basket"),
]