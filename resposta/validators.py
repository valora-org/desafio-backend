from django.db.models import Count, Q
from rest_framework import serializers

from resposta.models import Resposta


def max_resposta(self,value):
    itens = Resposta.objects.filter(questao=value).count()
    if itens >= 3:
        raise serializers.ValidationError('Essa Questão já possui 3 alternativa cadastradas')
