from rest_framework import generics
from django.shortcuts import get_object_or_404

from categories.models import Category
from categories.serializers import (
    QuizSerializer,
    DetailedQuizSerializer,
    LessDetailedQuizSerializer,
    RandomQuestionsQuizSerializer,
)
from utils.mixins import SerializerByMethodMixin
from questions.models import Question
from quizzes.models import Quiz


class QuizView(SerializerByMethodMixin, generics.ListCreateAPIView):
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
    queryset = Quiz.objects.all()
    serializer_map = {
        'GET': DetailedQuizSerializer,
        'PATCH': QuizSerializer,
        'PUT': QuizSerializer,
    }

    lookup_url_kwarg = 'quiz_id'


class RandomQuestionsQuizView(generics.ListAPIView):
    serializer_class = RandomQuestionsQuizSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        return Question.objects.filter(quiz=quiz).order_by('?')[:10]
