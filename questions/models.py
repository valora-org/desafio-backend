from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da categoria")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "category"

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name="Pergunta",
        null=True,
    )
    category = models.ForeignKey(
        "questions.Category",
        verbose_name="Categoria",
        on_delete=models.PROTECT,
        null=True,
    )
    registered_by = models.ForeignKey(
        "users.User",
        verbose_name="Usuário Criador",
        on_delete=models.DO_NOTHING,
    )
    first_answer = models.CharField(
        max_length=255,
        verbose_name="1ª Pergunta",
        null=True,
    )
    second_answer = models.CharField(
        max_length=255,
        verbose_name="2ª Pergunta",
        null=True,
    )
    third_answer = models.CharField(
        max_length=255,
        verbose_name="3ª Pergunta",
        null=True,
    )
    CHOICE_CORRECT_ANSWER = (
        ("1", "Primeira Pergunta"),
        ("2", "Segunda Pergunta"),
        ("3", "Terceira Pergunta"),
    )
    correct_answer = models.CharField(
        max_length=1,
        verbose_name="Resposta Correta",
        choices=CHOICE_CORRECT_ANSWER,
    )

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
        db_table = "question"

    def __str__(self) -> str:
        return self.question
