from django.urls import path
from .views.get_flight_info import get_flight_info
from .views.add_new_flight import add_new_flight
from .views.add_airport import add_airport
from .views.get_airport_info import get_airport_info

urlpatterns = [
    path("flights/<str:flight_number>/", get_flight_info, name="get_flight_info"),
    path("flights/", add_new_flight, name="add_new_flight"),
    path("airports/", add_airport, name="add_airport"),
    path("airports/<str:airport_code>/", get_airport_info, name="get_airport_info"),
]
