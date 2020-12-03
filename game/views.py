from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer
from .models import Category, Question, Answer
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('question')
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('answer')
    serializer_class = AnswerSerializer


