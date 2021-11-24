from django.db import models

from questao.models import Questao


class Resposta(models.Model):
    texto = models.TextField(max_length=255)
    questao = models.ForeignKey(Questao,related_name="respostas" ,on_delete=models.CASCADE)
    correta = models.BooleanField(default=False)
    def __str__(self):
        return '{id:%d,texto:%s}'% (self.id,self.texto)