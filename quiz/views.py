from rest_framework import viewsets
from rest_framework.response import Response
from quiz.models import Quiz, Question, Answer
from quiz.serializers import QuizSerializer, QuestionSerializer
import random


class QuizView(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def retrieve(self, request, format=None, pk=None):
        """
        Return one random question when quiz are called
        """
        question = Question.objects.filter(quiz__pk=pk).order_by('?')[:1]
        serializer = QuestionSerializer(question, context={'request': request}, many=True)
        return Response(serializer.data)