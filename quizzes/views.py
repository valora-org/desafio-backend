from django.shortcuts import get_object_or_404
from rest_framework import generics
# from rest_framework.views import APIView, Request, Response


from .models import Answer, Question, Quiz
from .serializers import AleatoryQuestionSerializer, QuizSerializer


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class AleatoryQuestion(generics.ListAPIView):
    serializer_class = AleatoryQuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        return Question.objects.filter(quiz=quiz)
