from collections import defaultdict
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, mixins, response, exceptions, permissions
from .models import Question, Quiz, Answer, Category, Score
from .serializers import (QuestionSerializer, QuestionListSerializer,
                          QuizListSerializer, QuizSerializer,
                          AnswerAdminSerializer, CategorySerializer,
                          QuestionCreateSerializer, GameCreateSerializer,
                          QuizResultSerializer)
from .permissions import IsAdmin, IsAdminOrReadOnly
from .mixins import ActionBasedSerializerMixin


class GameViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        game = GameCreateSerializer(data=request.data)
        game.is_valid(raise_exception=True)
        questions = Question.objects.random_questions(game.data['category'])

        quiz = Quiz()
        quiz.user = request.user
        quiz.category = Category.objects.get(slug=game.data['category'])
        quiz.save()
        quiz.questions.set(questions)

        return response.Response(QuizSerializer(quiz).data)

    def update(self, request, pk=None):
        queryset = Quiz.objects.filter(user=request.user, ended=False)
        quiz = get_object_or_404(queryset, pk=pk)

        answers: dict = request.data.get('answers')
        points = 0

        try:
            items = answers.items()
        except AttributeError:
            raise exceptions.ValidationError(
                                detail=_("Answers must be a dict."))

        answers_list = []
        for p, r in items:
            question = quiz.questions.get(pk=p)
            answer = question.answer_set.get(pk=r)
            answers_list.append(answer)

            if not question or not answer:
                raise exceptions.ValidationError(
                                detail=_("Erroneous question-answer pair."))

            answers[p] = answer.is_right

        for r in answers.values():
            if r:
                points += 1
            else:
                points -= 1
        score = Score(
            user=request.user,
            quiz=quiz,
            points=max(0, points)
        )
        score.save()
        quiz.ended = True
        quiz.answers.set(answers_list)
        quiz.save()

        result = QuizResultSerializer(quiz)
        res = result.data
        res.update({"score": score.points})

        return response.Response(res)


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


class AnswerViewSet(ActionBasedSerializerMixin, mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin, viewsets.GenericViewSet):
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


class RankingViewSet(viewsets.ViewSet):
    def list(self, request):
        scores = Score.objects.all()

        def make_scoreboard(scores):
            global_board = defaultdict(int)
            category_board = defaultdict(dict)

            for score in scores:
                username = score.user.username
                global_board[username] += score.points
                if score.quiz.category:
                    category = score.quiz.category.slug
                    category_board[category].update({
                        username: category_board[category].get(username, 0)+score.points
                    })

            return {"global": global_board, "categories": category_board}

        board = make_scoreboard(scores)

        return response.Response(board)
