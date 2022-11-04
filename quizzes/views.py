from rest_framework import generics
from django.shortcuts import get_object_or_404

from questions.models import Question
from .models import Quiz
from .serializers import QuizSerializer, RandomQuizQuestionsSerializer


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuizQuestionsView(generics.ListAPIView):
    serializer_class = RandomQuizQuestionsSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        return Question.objects.filter(quiz=quiz).order_by('?')[:10]
