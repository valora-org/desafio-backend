from django.db import models
from uuid import uuid4


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    question = models.ForeignKey(
        to='questions.Question',
        on_delete=models.CASCADE,
        related_name='answers',
    )

    def __repr__(self) -> str:
        return '<Answer %s - %s>' % (self.id, self.answer)

    def __str__(self) -> str:
        return self.answer
