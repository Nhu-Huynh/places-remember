from django.urls import path

from . import views

app_name = "places"

urlpatterns = [
    path("new/", views.place_new_view, name="place_new"),
    path("edit/<int:place_id>/", views.place_update_view, name="place_update"),
    path("delete/<int:place_id>/", views.place_delete_view, name="place_delete"),
]
