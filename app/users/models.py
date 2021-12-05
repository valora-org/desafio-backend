from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser, models.Model):

    username = models.CharField(max_length=250, blank=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
