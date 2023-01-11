from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    
    type_text = models.CharField(verbose_name="Tipo da Categoria", max_length=100)

    class Meta:
        ordering = ("id",)
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")

    def __str__(self) -> str:
        return self.type_text


class Question(models.Model):
    
    question_choices = (
        ("first_choice", "Primeira escolha"),
        ("second_choice", "Segunda escolha"),
        ("third_choice", "Terceira escolha")
    )
    
    category = models.ForeignKey(
        Category,
        verbose_name="Categoria",
        on_delete=models.CASCADE,
        related_name="question"
    )
    
    question_text = models.CharField(
        verbose_name="Texto da Pergunta",
        max_length=200
    )
    
    first_choice = models.CharField(
        verbose_name="Primeira Escolha",
        max_length=100
    )
    
    second_choice = models.CharField(
        verbose_name="Segunda Escolha",
        max_length=100
    )
    
    third_choice = models.CharField(
        verbose_name="Terceira Escolha",
        max_length=100
    )
    
    correct_choice = models.CharField(
        verbose_name="Escolha correta",
        max_length=100,
        choices=question_choices
    )
    
    class Meta:
        ordering = ("id",)
        verbose_name = _("Pergunta")
        verbose_name_plural = _("Perguntas")
    
    def __str__(self) -> str:
        return self.question_text

