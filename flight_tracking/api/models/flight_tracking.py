import uuid

from django.db import models

from .flight import Flight
from .user import User


class FlightTracking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracking_status = models.CharField(max_length=20, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    next_flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, null=True, blank=True
    )
    current_flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.flight

    class Meta:
        ordering = ("-create_date",)
