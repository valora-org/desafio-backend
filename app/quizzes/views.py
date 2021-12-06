import random

from django.db.models import query

from rest_framework import status, viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from app.permissions import IsAdmin

from quizzes.models import Answer, Question, Ranking
from quizzes.serializers import AnswerSerializer, QuestionSerializer, RankingSerializer, QuizQuestionSerializer

from categories.models import Category


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def create(self, request, *args, **kwargs):
        if not "answers" in request.data:
            return Response(data="Missig answers on payload.", status=400)

        answers = request.data["answers"]
        return_payload = []

        serialized_data = self.serializer_class(data=answers, many=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(data=serialized_data.data, status=201)

    def update(self, request, *args, **kwargs):
        answer = self.get_object()
        if not "text" in request.data and not "is_correct" in request.data:
            return Response(data="Missig field.", status=400)

        if "text" in request.data:
            answer.text = request.data["text"]

        if "is_correct" in request.data:
            answer.is_correct = request.data["is_correct"]

        answer.save()

        return Response(data=self.serializer_class(instance=answer).data, status=200)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def update(self, request, *args, **kwargs):
        question = self.get_object()
        if not "text" in request.data and not "category" in request.data:
            return Response(data="Missig field.", status=400)

        if "text" in request.data:
            question.text = request.data["text"]

        if "category" in request.data:
            question.category = request.data["category"]

        question.save()

        return Response(data=self.serializer_class(instance=question).data, status=200)


class GetQuizViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = QuizQuestionSerializer
    queryset = Question.objects.all()

    def get_quiz(self, request, *args, **kwargs):
        category = request.query_params.get("category", None)

        if category is None:
            return Response(data="Missing category.", status=400)

        if not Category.objects.filter(name=category).exists():
            return Response(data="Given category is invalid.", status=400)

        questions = list(Question.objects.filter(
            category__name=category).values_list("id", flat=True))

        random_questions = random.sample(questions, 10)

        questions_qs = Question.objects.filter(id__in=random_questions)

        return Response(data=self.serializer_class(questions_qs, many=True).data, status=200)


class RankingViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RankingSerializer
    queryset = Ranking.objects.all()

    def list(self, request, *args, **kwargs):
        category = request.query_params.get("category", None)

        if category is not None:
            if not Category.objects.filter(name=category).exists():
                return Response(data="Given category is invalid.", status=400)
            qs = self.get_queryset().filter(category__name=category)
            return Response(data=self.serializer_class(qs, many=True).data, status=200)

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if not "ids" in request.data:
            return Response(data="Missing answers.", status=400)

        answer_ids = request.data["ids"]

        questions = Question.objects.filter(answers__id__in=answer_ids)

        if questions.count() != 10:
            return Response(data="Invalid payload. Not enought questions answered", status=400)

        category = questions.values_list(
            "category_id", flat=True).distinct()

        if category.count() != 1:
            return Response(data="Answers are from questions of different categories.", status=400)

        correct_answers_count = Answer.objects.filter(
            id__in=answer_ids, is_correct=True).count()
        score = correct_answers_count - (10 - correct_answers_count)
        if score < 0:
            score = 0

        data = {"user": request.user.id,
                "score": score, "category": category[0]}

        serialized_data = self.serializer_class(data=data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()

            created_at = serialized_data.data["created_at"]
            global_rank = Ranking.objects.filter(
                score__gte=score, created_at__lt=created_at).count() + 1

            return Response(data={"global_rank": global_rank, "score": score}, status=201)
