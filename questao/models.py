from django.db import models

from categoria.models import Categoria


class Questao(models.Model):
    texto = models.TextField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{id:%d,texto:%s}'% (self.id,self.texto)