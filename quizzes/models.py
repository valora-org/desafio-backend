from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    questions = models.ManyToManyField("questions.Question", related_name="Quizzes")
