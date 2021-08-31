from rest_framework import viewsets
from rest_framework import permissions

from quiz import serializers
from quiz import models
import quiz.permissions


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        quiz.permissions.IsAdmin,
    ]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        quiz.permissions.IsAdmin,
    ]

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        quiz.permissions.IsAdmin,
    ]

    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
