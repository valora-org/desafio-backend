from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsAdminOrReadOnly
from questions.models import Question
from questions.serializers import (
    DetailedQuestionSerializer,
    LessDetailedQuestionSerializer,
    QuestionSerializer,
)
from quizzes.models import Quiz
from utils.mixins import SerializerByMethodMixin


class QuestionView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Question.objects.all()

    serializer_map = {
        'GET': LessDetailedQuestionSerializer,
        'POST': QuestionSerializer,
    }

    def perform_create(self, serializer):
        quiz_id = self.request.data['quiz']
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        serializer.save(quiz=quiz)


class QuestionDetailView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Question.objects.all()

    serializer_map = {
        'GET': DetailedQuestionSerializer,
        'PATCH': LessDetailedQuestionSerializer,
        'PUT': LessDetailedQuestionSerializer,
    }

    lookup_field = 'id'
