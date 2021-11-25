from django.contrib.auth.models import User
from django.db import models

from categoria.models import Categoria
from questao.models import Questao


class Jogo(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False)
    nota = models.PositiveSmallIntegerField(null=True)
    questoes = models.ManyToManyField(Questao,)
