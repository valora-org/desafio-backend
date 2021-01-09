from rest_framework import viewsets
from apps.quiz.models import Category, Match, Selection
from apps.quiz.serializer import CategorySerializer, MatchSerializer, SelectionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Show Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MatchViewSet(viewsets.ModelViewSet):
    """Show Match"""
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class SelectionViewSet(viewsets.ModelViewSet):
    """Show Selection"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
