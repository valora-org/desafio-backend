from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name_plural = _('Categories')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return '<Category %s - %s>' % (self.id, self.name)


class Quiz(models.Model):
    class Meta:
        verbose_name_plural = _('Quizzes')
        # ordering = ('id')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        to='quizzes.Category',
        on_delete=models.DO_NOTHING,
        related_name='quizzes',
    )

    def __repr__(self) -> str:
        return '<Quiz %s - %s>' % (self.id, self.name)


class Levels(models.TextChoices):
    EASY = 'Fácil'
    MODERATE = 'Moderado'
    HARD = 'Difícil'
    VERY_HARD = 'Muito Difícil'


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question = models.CharField(max_length=200)
    level = models.CharField(
        max_length=16, choices=Levels.choices, default=Levels.MODERATE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    quiz = models.ForeignKey(
        to='quizzes.Quiz',
        on_delete=models.DO_NOTHING,
        related_name='questions',
    )

    def __repr__(self) -> str:
        return '<Question %s - %s>' % (self.id, self.question)


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    question = models.ForeignKey(
        to='quizzes.Question',
        on_delete=models.CASCADE,
        related_name='answers',
    )

    def __repr__(self) -> str:
        return '<Answer %s - %s>' % (self.id, self.answer)
