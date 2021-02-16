from rest_framework import viewsets, mixins
from .models import Question, Quiz, Answer, Category
from .serializers import (QuestionSerializer, QuestionListSerializer,
                          QuizListSerializer, QuizSerializer,
                          AnswerAdminSerializer, CategorySerializer,
                          QuestionCreateSerializer)
from .permissions import IsAdmin, IsAdminOrReadOnly
from .mixins import ActionBasedSerializerMixin


class QuestionViewSet(ActionBasedSerializerMixin, viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAdmin]
    serializer_classes = {
        'list': QuestionListSerializer,
        'create': QuestionCreateSerializer,
        'update': QuestionCreateSerializer,
        'default': QuestionSerializer
    }


class QuizViewSet(ActionBasedSerializerMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_classes = {
        'list': QuizListSerializer,
        'default': QuizSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        return queryset


class AnswerViewSet(ActionBasedSerializerMixin, viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [IsAdmin]
    serializer_classes = {
        'default': AnswerAdminSerializer
    }


class CategoryViewSet(ActionBasedSerializerMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_classes = {
        'default': CategorySerializer
    }
