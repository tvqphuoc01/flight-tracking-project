from django.urls import path
from .views.get_flight_info import get_flight_info
from .views.add_new_flight import add_new_flight

urlpatterns = [
    path("flights/<str:flight_id>/", get_flight_info, name="get_flight_info"),
    path("flights/", add_new_flight, name="add_new_flight"),
]
