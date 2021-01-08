from rest_framework import viewsets
from apps.quiz.models import Match
from apps.quiz.serializer import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    """Exibindo partidas"""
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
