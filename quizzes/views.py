from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from categories.models import Category
from categories.serializers import (
    DetailedQuizSerializer,
    LessDetailedQuizSerializer,
    QuizSerializer,
    RandomQuestionsQuizSerializer,
)
from core.permissions import IsAdminOrReadOnly
from questions.models import Question
from questions.serializers import QuizQuestionSerializer
from quizzes.models import Quiz
from utils.mixins import SerializerByMethodMixin


class QuizView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Quiz.objects.all()

    serializer_map = {
        'GET': QuizSerializer,
        'POST': LessDetailedQuizSerializer,
    }

    def perform_create(self, serializer):
        category_id = self.request.data['category']
        category = get_object_or_404(Category, pk=category_id)
        serializer.save(category=category)


class QuizDetailView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Quiz.objects.all()

    serializer_map = {
        'GET': DetailedQuizSerializer,
        'PATCH': QuizSerializer,
        'PUT': QuizSerializer,
    }

    lookup_field = 'id'


class RandomQuestionsQuizView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    serializer_class = RandomQuestionsQuizSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        return Question.objects.filter(quiz=quiz).order_by('?')[:10]


class QuizQuestion(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    serializer_class = QuizQuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        return Question.objects.filter(quiz=quiz)
