import uuid

from django.db import models


class Airport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icao = models.CharField(max_length=4, unique=True, null=True, blank=True)
    iata = models.CharField(max_length=3, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country_ip = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
