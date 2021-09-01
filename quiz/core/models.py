from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)


class Question(models.Model):
    question = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
