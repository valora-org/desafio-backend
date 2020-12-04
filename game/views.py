from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer, UserSerializer, GroupSerializer
from .models import Category, Question, Answer

from django.contrib.auth.models import User, Group
from rest_framework import permissions

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




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


