from django.db import models

from questao.models import Questao


class Resposta(models.Model):
    texto = models.TextField(max_length=255)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    correta = models.BooleanField(default=False)
    def __str__(self):
        return f'categoria:{self.id} texto:{self.texto}'