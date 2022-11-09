from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import get_object_or_404
from .serializers import QuizSerializer
from questions.models import Question
from django.db import IntegrityError
from django.http import Http404
from users.models import User
from .models import Quiz
import random


class QuizView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, _):

        quizzes = Quiz.objects.all()

        quizzes_serialized = QuizSerializer(quizzes, many=True)

        return Response({"quizzes": quizzes_serialized.data}, status=status.HTTP_200_OK)

    def post(self, request: Request):

        try:
            quiz_serialized = QuizSerializer(data=request.data)
            quiz_serialized.is_valid(raise_exception=True)
            quiz_serialized.save()

            return Response(quiz_serialized.data, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response(
                {"message": "A quiz with the provided title already exists"},
                status=status.HTTP_409_CONFLICT,
            )

        except MultipleObjectsReturned:
            return Response(
                {"message": "JSON malformatted"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class QuizSoloView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, _, quiz_id: int):

        try:
            quiz = get_object_or_404(Quiz, id=quiz_id)
            quiz_serialized = QuizSerializer(quiz)

            return Response({"quiz": quiz_serialized.data}, status=status.HTTP_200_OK)

        except Http404:
            return Response(
                {"message": "quiz not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, quiz_id: int):

        try:
            quiz = get_object_or_404(Quiz, id=quiz_id)
            quiz_serialized = QuizSerializer(quiz, request.data, partial=True)
            quiz_serialized.is_valid(raise_exception=True)
            quiz_serialized.save()

            return Response({"quiz": quiz_serialized.data}, status=status.HTTP_200_OK)

        except Http404:
            return Response(
                {"message": "quiz not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except KeyError as error:
            return Response(
                {"Missing fields": error.args}, status=status.HTTP_400_BAD_REQUEST
            )

        except MultipleObjectsReturned:
            return Response(
                {"message": "JSON malformatted"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, _, quiz_id: int):

        try:
            quiz = get_object_or_404(Quiz, id=quiz_id)
            quiz.delete()

            return Response("", status=status.HTTP_204_NO_CONTENT)

        except Http404:
            return Response(
                {"message": "quiz not found"}, status=status.HTTP_404_NOT_FOUND
            )
