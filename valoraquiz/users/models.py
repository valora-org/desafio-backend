from django.db import models
from django.contrib.auth.models import AbstractUser
from . import choices


class User(AbstractUser):
    type = models.CharField(
        max_length=6, choices=choices.TYPE_CHOICES, default=choices.PLAYER
    )
