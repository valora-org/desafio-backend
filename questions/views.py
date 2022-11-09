from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import get_object_or_404
from .serializers import QuestionSerializer
from django.http import Http404
from .models import Question


class QuestionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, _):

        questions = Question.objects.all()
        questions_serialized = QuestionSerializer(questions, many=True)

        return Response(
            {"questions": questions_serialized.data}, status=status.HTTP_200_OK
        )

    def post(self, request: Request):

        question_serialized = QuestionSerializer(data=request.data)
        question_serialized.is_valid(raise_exception=True)
        question_serialized.save()

        return Response(question_serialized.data, status=status.HTTP_201_CREATED)


class QuestionSoloView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, _, question_id: int):

        try:
            question = get_object_or_404(Question, id=question_id)
            question_serialized = QuestionSerializer(question)

            return Response(
                {"question": question_serialized.data}, status=status.HTTP_200_OK
            )

        except Http404:
            return Response(
                {"message": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request: Request, question_id: int):

        try:
            question = get_object_or_404(Question, id=question_id)
            question_serialized = QuestionSerializer(
                question, request.data, partial=True
            )
            question_serialized.is_valid(raise_exception=True)
            question_serialized.save()

            return Response(
                {"question": question_serialized.data}, status=status.HTTP_200_OK
            )

        except Http404:
            return Response(
                {"message": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except MultipleObjectsReturned:
            return Response(
                {"message": "alternative(s) malformatted"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, _, question_id: int):

        try:
            question = get_object_or_404(Question, id=question_id)
            question.delete()

            return Response("", status=status.HTTP_204_NO_CONTENT)

        except Http404:
            return Response(
                {"message": "question not found"}, status=status.HTTP_404_NOT_FOUND
            )
