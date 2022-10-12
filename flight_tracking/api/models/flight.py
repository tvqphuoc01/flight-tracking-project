import uuid

from django.db import models

from .country import Country
from .airport import Airport
from .airline import Airline
from .aircraft import Aircraft


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft_type = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    airline = models.ForeignKey(
        Airline, on_delete=models.CASCADE, null=True, blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    country_departure = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
    country_arrival = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.IntegerField(default=0)
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.flight_number

    class Meta:
        ordering = ("-create_date",)
