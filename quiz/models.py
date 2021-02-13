from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=300)


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Quiz(models.Model):
    questions = models.ManyToManyField(Question)


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
