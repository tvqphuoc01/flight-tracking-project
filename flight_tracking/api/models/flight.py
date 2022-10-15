import uuid

from django.db import models

from .airport import Airport
from .airline import Airline
from .aircraft import Aircraft


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    aircraft_type = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, null=True, blank=True
    )
    airline = models.ForeignKey(
        Airline, on_delete=models.CASCADE, null=True, blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    country_departure = models.CharField(max_length=3, null=True, blank=True)
    country_arrival = models.CharField(max_length=3, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.flight_number

    class Meta:
        ordering = ("-create_date",)
