from users.models import User
from django.db import models
from django.db.models.deletion import CASCADE

from rest_framework.validators import ValidationError


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

    def save(self, *args, **kwargs):
        question_answers = self.question.answer_set.all()
        if question_answers.count() >= 3:
            raise ValidationError({"error": "Question already has 3 answers"})

        if self.is_right and (
            True in question_answers.values_list("is_right", flat=True)
        ):
            raise ValidationError("Question already has right answer")

        if (
            question_answers.count() == 2
            and not self.is_right
            and (True not in question_answers.values_list("is_right", flat=True))
        ):
            raise ValidationError(
                "Question has only incorrect answers, please provide a correct answer"
            )

        super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        return self.label


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    questions = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
