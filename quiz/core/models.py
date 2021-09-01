from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)