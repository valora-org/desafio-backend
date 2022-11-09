from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    class Meta:
        verbose_name_plural = _('Quizzes')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.DO_NOTHING,
        related_name='quizzes',
    )

    def __repr__(self) -> str:
        return '<Quiz %s - %s>' % (self.id, self.name)

    def __str__(self) -> str:
        return self.name
