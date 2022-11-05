from django.db import models
from uuid import uuid4


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
    is_active = models.BooleanField()

    quiz = models.ForeignKey(
        to='quizzes.Quiz',
        on_delete=models.DO_NOTHING,
        related_name='questions',
    )

    def __repr__(self) -> str:
        return '<Question %s - %s>' % (self.id, self.question)
