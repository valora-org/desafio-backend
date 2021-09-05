from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255, default='A1')
    answer2 = models.CharField(max_length=255, default='A2')
    answer3 = models.CharField(max_length=255, default='A3')
    right_answer = models.CharField(max_length=2, default='A1', choices=[
        ('A1', 'answer1'),
        ('A2', 'answer2'),
        ('A3', 'answer3'),
    ])

    def __str__(self):
        return self.question


class Result(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
