from django.shortcuts import get_object_or_404
from rest_framework import generics

from questions.models import Question
from questions.serializers import (
    DetailedQuestionSerializer,
    LessDetailedQuestionSerializer,
)
from quizzes.models import Quiz
from utils.mixins import SerializerByMethodMixin


class QuestionView(SerializerByMethodMixin, generics.ListCreateAPIView):
    serializer_class = DetailedQuestionSerializer
    queryset = Question.objects.all()

    serializer_map = {
        'GET': LessDetailedQuestionSerializer,
        'POST': DetailedQuestionSerializer,
    }

    def perform_create(self, serializer):
        quiz_id = self.request.data['quiz']
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        serializer.save(quiz=quiz)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessDetailedQuestionSerializer
    queryset = Question.objects.all()

    lookup_field = 'id'
