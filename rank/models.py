from django.db import models


class Rank(models.Model):
    score = models.PositiveIntegerField(
        verbose_name="Pontuação",
        null=True,
    )
    category = models.ForeignKey(
        "questions.Category",
        verbose_name="Categoria",
        on_delete=models.PROTECT,
        null=True,
    )
    profile = models.ForeignKey(
        "users.User",
        verbose_name="Usuário",
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        verbose_name = "Rank"
        verbose_name_plural = "Rank"
        db_table = "rank"

    def __str__(self) -> str:
        return f"{self.profile} - {self.score}"
