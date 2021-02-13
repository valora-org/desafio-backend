from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'admin'
    PLAYER = 'player'

    TYPE_CHOICES = (
        (ADMIN, "Admin"),
        (PLAYER, "Player")
    )

    type = models.CharField(choices=TYPE_CHOICES, max_length=6,
                            default=PLAYER)
