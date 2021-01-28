from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.views.generic import ListView
from quiz_api.models import Pergunta, Classificacao
from .serializers import PerguntaSerializer, ClassificacaoSerializer
from django.shortcuts import render


class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'nome_classificacao']


class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'classificacao', 'pergunta']
