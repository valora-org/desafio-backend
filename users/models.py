from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=128)
    points = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()
