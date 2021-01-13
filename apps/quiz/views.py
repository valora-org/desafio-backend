from rest_framework import viewsets, generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from apps.quiz.models import Category, MatchGame, Selection
from apps.quiz.serializer import CategorySerializer, MatchGameSerializer, SelectionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MatchGameViewSet(viewsets.ModelViewSet):
    """CRUD Match"""
    queryset = MatchGame.objects.all()
    serializer_class = MatchGameSerializer


class SelectionViewSet(viewsets.ModelViewSet):
    """CRUD Selections"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class MatchesGameFilterCategoryAPIView(generics.ListAPIView):
    """get Matches per Category"""
    queryset = MatchGame.objects.all()
    serializer_class = MatchGameSerializer

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            return self.queryset.filter(category_id=self.kwargs.get('category_pk'))
