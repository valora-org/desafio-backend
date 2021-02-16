from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, mixins, response, exceptions
from .models import Question, Quiz, Answer, Category, Score
from .serializers import (QuestionSerializer, QuestionListSerializer,
                          QuizListSerializer, QuizSerializer,
                          AnswerAdminSerializer, CategorySerializer,
                          QuestionCreateSerializer, GameCreateSerializer)
from .permissions import IsAdmin, IsAdminOrReadOnly
from .mixins import ActionBasedSerializerMixin


class GameViewSet(viewsets.ViewSet):
    def create(self, request):
        game = GameCreateSerializer(data=request.data)
        game.is_valid(raise_exception=True)
        questions = Question.objects.filter(
            category__slug=game.data['category']
        )

        quiz = Quiz()
        quiz.user = request.user
        quiz.save()
        quiz.questions.set(questions)

        return response.Response(QuizSerializer(quiz).data)

    def retrieve(self, request, pk=None):
        queryset = Quiz.objects.filter(user=request.user)
        quiz = get_object_or_404(queryset, pk=pk)
        serializer = QuizSerializer(quiz)
        return response.Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Quiz.objects.filter(user=request.user, ended=False)
        quiz = get_object_or_404(queryset, pk=pk)

        answers: dict = request.data.get('answers')
        finished = request.data.get('finished')
        points = 0

        try:
            items = answers.items()
        except AttributeError:
            raise exceptions.ValidationError(
                                detail=_("Answers must be a dict."))

        for p, r in items:
            question = quiz.questions.get(pk=p)
            answer = question.answer_set.get(pk=r)

            if not question or not answer:
                raise exceptions.ValidationError(
                                detail=_("Erroneous question-answer pair."))

            if finished:
                answers[p] = answer.is_right
                points += 1

        if finished:
            quiz.ended = True
            quiz.save()
            score = Score(
                user=request.user,
                quiz=quiz,
                points=points
            )
            score.save()

        return response.Response(answers)


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
