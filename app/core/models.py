from uuid import uuid4
from django.core.exceptions import RequestAborted
from django.db import models
from django.contrib.auth.models import User, AbstractUser



class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

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
    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{self.name.upper()}'



class QuestionModel(Base):
    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
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

class CategoryQuestionModel(Base):
    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,

    )
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Categoria e Pergunta'
        verbose_name_plural = 'Categorias e Perguntas'
        unique_together = (("category", "question"),)
    
    def __str__(self):
        return f'{self.category.name} - {self.question}'


class AnswerModel(Base):
    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
    question = models.ForeignKey(
        QuestionModel,
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
    correct_answer = models.BooleanField(
        'Resposta Correta?',
        default=False,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        is_correct = 'Correta' if self.correct_answer is True else 'Incorreta'
        return f'{self.question} {self.answer} - {is_correct}'


class RankingModel(Base):
    id = models.UUIDField('ID', primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    value = models.IntegerField('Acertos', blank=False, null=False)

    class Meta:
        verbose_name = 'Ranking'
        verbose_name_plural = 'Ranking'
        unique_together = (("category", "user"),)

    def __str__(self):
        return f' - {self.category.name} - {self.value}'

