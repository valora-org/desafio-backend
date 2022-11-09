from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    quizzes = models.ManyToManyField("quizzes.Quiz", related_name="categories")
