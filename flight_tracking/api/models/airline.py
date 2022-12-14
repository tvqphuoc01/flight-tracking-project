import uuid

from django.db import models


class Airline(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country_ip = models.CharField(max_length=3, null=True, blank=True)
    logo_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
