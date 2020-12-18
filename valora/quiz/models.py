from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quiz(models.Model):

    ANSWER_CHOICES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    )

    category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=400, blank=False, null=False)
    answer_A = models.CharField(max_length=200, blank=False, null=False)
    answer_B = models.CharField(max_length=200, blank=False, null=False)
    answer_C = models.CharField(max_length=200, blank=False, null=False)
    right_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES, blank=False, null=False)

    def __str__(self):
        return "{0} - {1}".format(self.category, self.question)


class Results(models.Model):

    quiz = models.ForeignKey(Quiz, related_name='quiz', on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    answer = models.BooleanField()

    def __str__(self):
        _answer = "Incorrect"
        if self.answer:
            resposta = "Correct"

        return "Result: {0} - {1} - {2}".format(self.quiz, self.author.username, resposta)

