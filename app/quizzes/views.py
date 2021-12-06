from functools import partial
import random

from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from app.permissions import IsAdmin

from quizzes.models import Answer, Question, Ranking
from quizzes.serializers import AnswerSerializer, QuestionSerializer, RankingSerializer, QuizQuestionSerializer

from categories.models import Category


# Answer View with support for create, update, delete and
# list answers. Only authenticated admins can use these endpoints.
class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    # Expected payload is a dict with key answers and it's value
    # being an array of dicts. It is expected that each dict
    # contains the data to create an answer (text-str, question id-int and is_correct-bool)
    def create(self, request, *args, **kwargs):
        # Check if payload contains the answers to be created
        if not "answers" in request.data:
            return Response(data="Missig answers on payload.", status=400)

        answers = request.data["answers"]
        return_payload = []

        question_id = answers[0]["question"]

        if not (Answer.objects.filter(question=question_id).count() + len(answers)) <= 3:
            return Response(data="Too many answers for this question.", status=400)

        serialized_data = self.serializer_class(data=answers, many=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(data=serialized_data.data, status=201)

    # Expect either text-str or is_correct-bool or both in the payload
    def update(self, request, pk, *args, **kwargs):
        answer = self.get_object()

        # Check if there is at least one field that is allowed to be updated in the payload
        if not "text" in request.data and not "is_correct" in request.data:
            return Response(data="Missig field.", status=400)

        data = {}

        # Prepare data to update answer
        if "text" in request.data:
            data["text"] = request.data["text"]

        if "is_correct" in request.data:
            data["is_correct"] = request.data["is_correct"]

        data["id"] = pk

        answer = Answer.objects.get(id=pk)

        serialized_data = self.serializer_class(
            answer, data=data, partial=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(data=serialized_data.data, status=200)


# Question View with support for create, update, delete and
# list questions. Only authenticated admins can use these endpoints.
class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    # Expect either text-str or category id-int or both in the payload
    def update(self, request, pk, *args, **kwargs):
        question = self.get_object()
        if not "text" in request.data and not "category" in request.data:
            return Response(data="Missig field.", status=400)

        data = {}

        # Prepare data to update question
        if "text" in request.data:
            data["text"] = request.data["text"]

        if "category" in request.data:
            if not Category.objects.filter(id=request.data["category"]).exists():
                return Response(data="Invalid category id.", status=400)
            data["category"] = request.data["category"]

        data["id"] = pk

        question = Question.objects.get(id=pk)

        serialized_data = self.serializer_class(
            question, data=data, partial=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(data=serialized_data.data, status=200)


# Generate Quiz View. It's used to generate a quiz with 10
# questions from the same category. Only authenticated
# users can use these endpoints.
class GetQuizViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = QuizQuestionSerializer
    queryset = Question.objects.all()

    # Expects a category name-str in the query params
    def get_quiz(self, request, *args, **kwargs):
        category = request.query_params.get("category", None)

        # Check if a category was passed
        if category is None:
            return Response(data="Missing category.", status=400)

        # Check if the given category exists
        if not Category.objects.filter(name=category).exists():
            return Response(data="Given category is invalid.", status=400)

        questions = list(Question.objects.filter(
            category__name=category).values_list("id", flat=True))

        # Check if there is at least 10 questions from the given category
        if len(questions) < 10:
            return Response(data="Not enought questions of given category. Aborting", status=400)

        # Randomize the questions
        random_questions = random.sample(questions, 10)

        questions_qs = Question.objects.filter(id__in=random_questions)

        return Response(data=self.serializer_class(questions_qs, many=True).data, status=200)


# Ranking View with support for create an entry in the ranking
# table and list the ranking globally or based on category.
# Only authenticated users can use these endpoints.
class RankingViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RankingSerializer
    queryset = Ranking.objects.all()

    def list(self, request, *args, **kwargs):
        category = request.query_params.get("category", None)

        # Check if a category was given
        if category is not None:
            # Check if given category is valid before filtering
            if not Category.objects.filter(name=category).exists():
                return Response(data="Given category is invalid.", status=400)
            qs = self.get_queryset().filter(category__name=category)
            return Response(data=self.serializer_class(qs, many=True).data, status=200)

        return super().list(request, *args, **kwargs)

    # Expected payload is a dict with key ids and it's value
    # being an array of ints corresponding to existing answers.
    def create(self, request, *args, **kwargs):
        # Check if payload contains key ids
        if not "ids" in request.data:
            return Response(data="Missing answers.", status=400)

        answer_ids = request.data["ids"]

        questions = Question.objects.filter(answers__id__in=answer_ids)

        # Check if given answer ids correspond to 10 different questions
        if questions.count() != 10:
            return Response(data="Invalid payload. Not enought questions answered", status=400)

        category = questions.values_list(
            "category_id", flat=True).distinct()

        # Confirm that all questions were from the same category
        if category.count() != 1:
            return Response(data="Answers are from questions of different categories.", status=400)

        # Calculate score
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
