from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    # path('', views.places_list, name='list'),
    path('new/', views.place_new, name='new'),
    # path('<slug:slug>', views.place_page, name='page'),
]
