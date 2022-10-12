import uuid

from django.db import models

from .airline import Airline


class Aircraft(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aircraft_type = models.CharField(max_length=50)
    aircraft_registration = models.CharField(max_length=10)
    airline = models.ForeignKey(
        Airline, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.aircraft_type

    class Meta:
        ordering = ("id",)
