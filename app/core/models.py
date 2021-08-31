from uuid import uuid4
from django.core.exceptions import RequestAborted
from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        abstract = True


class CategoryModel(Base):
    id = models.UUIDField('ID', primary_key=True, default=uuid4)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{self.name.upper()}'


class AnswerModel(Base):
    id = models.UUIDField('ID',primary_key=True, default=uuid4)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    answer = models.CharField(
        'Resposta',
        max_length=200,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return f'{self.answer}'


class QuestionModel(Base):
    id = models.UUIDField('ID', primary_key=True, default=uuid4)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    answer = models.ForeignKey(
        AnswerModel,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )
    question = models.CharField(
        'Pergunta',
        max_length=200,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return f'{self.question}'

