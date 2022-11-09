from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from answers.models import Answer
from core.permissions import IsAdminOrReadOnly
from questions.models import Question
from questions.serializers import AnswerSerializer, DetailedAnswerSerializer
from utils.mixins import SerializerByMethodMixin


class AnswerView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Answer.objects.all()

    serializer_map = {
        'GET': DetailedAnswerSerializer,
        'POST': AnswerSerializer,
    }

    def perform_create(self, serializer):
        question_id = self.request.data['question']
        question = get_object_or_404(Question, pk=question_id)
        serializer.save(question=question)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Answer.objects.all()
    serializer_class = DetailedAnswerSerializer

    lookup_field = 'id'
