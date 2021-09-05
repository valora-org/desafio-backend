from quiz.core.models import Category, Question
from quiz.core.serializers import CategorySerializer, QuestionSerializer
from rest_framework import viewsets
from rest_framework import permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]
    