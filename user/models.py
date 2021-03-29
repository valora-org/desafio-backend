from django.contrib.auth.models import AbstractUser
from django.db import models


class Point(models.Model):
    category = models.IntegerField()
    points = models.IntegerField(default=0)
    global_point = models.IntegerField(default=0)


class User(AbstractUser):
    points = models.ManyToManyField(Point)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email