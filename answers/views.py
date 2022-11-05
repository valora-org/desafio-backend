from django.shortcuts import get_object_or_404
from rest_framework import generics

from utils.mixins import SerializerByMethodMixin
from answers.models import Answer
from questions.models import Question
from questions.serializers import AnswerSerializer, DetailedAnswerSerializer


class AnswerView(SerializerByMethodMixin, generics.ListCreateAPIView):
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
    serializer_class = DetailedAnswerSerializer
    queryset = Answer.objects.all()

    lookup_field = 'id'
