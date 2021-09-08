from quiz import models
from rest_framework import viewsets
from rest_framework import permissions
from quiz.api import serializers
from rest_framework.filters import SearchFilter

class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ('id', 'user', 'score', 'category')
    filter_backends =  (SearchFilter,)
    search_fields = ('user', 'score', 'category')

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ('id', 'question', 'true_answer')

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ('id', 'answer')

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_fields = ('id', 'role', 'username')
    filter_backends =  (SearchFilter,)
    search_fields = ('role', 'username')
    permission_classes = [permissions.IsAuthenticated]