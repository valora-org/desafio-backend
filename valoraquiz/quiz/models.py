from users.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    label = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Answer(models.Model):
    label = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=CASCADE)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    questions = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
