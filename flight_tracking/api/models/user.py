import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from api.models.country import Country


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    profile_picture_url = models.CharField(max_length=500, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
