from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)
