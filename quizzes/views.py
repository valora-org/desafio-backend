from rest_framework import generics
from django.shortcuts import get_object_or_404

from categories.serializers import (
    QuizSerializer,
    RandomQuestionsQuizSerializer,
)
from questions.models import Question
from quizzes.models import Quiz


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestionsQuizView(generics.ListAPIView):
    serializer_class = RandomQuestionsQuizSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        return Question.objects.filter(quiz=quiz).order_by('?')[:10]
