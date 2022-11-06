from django.shortcuts import get_object_or_404
from rest_framework import generics

from questions.models import Question
from questions.serializers import (
    DetailedQuestionSerializer,
    LessDetailedQuestionSerializer,
    QuestionSerializer,
)
from quizzes.models import Quiz
from utils.mixins import SerializerByMethodMixin


class QuestionView(SerializerByMethodMixin, generics.ListCreateAPIView):
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
    queryset = Question.objects.all()

    serializer_map = {
        'GET': DetailedQuestionSerializer,
        'PATCH': LessDetailedQuestionSerializer,
        'PUT': LessDetailedQuestionSerializer,
    }

    lookup_url_kwarg = 'question_id'
