from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import views
from rest_framework import response
from rest_framework import status

from quiz import services
from quiz import serializers
from quiz import models
import quiz.permissions


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        quiz.permissions.IsAdmin,
    ]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        quiz.permissions.IsAdmin,
    ]

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        quiz.permissions.IsAdmin,
    ]

    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class QuizViewSet(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request):
        serializer = serializers.QuizCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            quiz = services.create_quiz(
                category_id=serializer.data["category_id"], user=request.user
            )
        except ValueError as error:
            return response.Response(
                {"error": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = serializers.QuizDetailSerializer(quiz)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, quiz_id=None):
        if quiz_id:
            return self._detail(quiz_id=quiz_id, user_id=request.user.pk)

        return self._list(user_id=request.user.pk)

    def _detail(self, quiz_id, user_id):
        quiz = services.get_quiz_by_id_and_user_id(pk=quiz_id, user_id=user_id)

        if not quiz:
            return response.Response(
                {"error": "Quiz not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = serializers.QuizDetailSerializer(quiz)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def _list(self, user_id):
        quizzes = services.filter_quiz_by_user_id(user_id=user_id)

        serializer = serializers.QuizDetailSerializer(quizzes, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, quiz_id):

        serializer = serializers.QuizAnsweredSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        quiz = services.get_quiz_by_id_and_user_id(pk=quiz_id, user_id=request.user.pk)

        if not quiz:
            return response.Response(
                {"error": "Quiz not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        updated_quiz = services.update_quiz_answered(
            quiz=quiz,
            answers=serializer.data["answers"],
            is_finished=serializer.data["is_finished"],
        )

        serializer = serializers.QuizDetailSerializer(updated_quiz)

        return response.Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, quiz_id):
        quiz = services.get_quiz_by_id_and_user_id(quiz_id, user_id=request.user.pk)

        if not quiz:
            return response.Response(
                {"error": "Quiz not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        quiz.delete()

        return response.Response(None, status=status.HTTP_204_NO_CONTENT)


class RankingViewSet(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, category_id=None):
        if category_id:
            return self.ranking_by_category(category_id=category_id)

        return self.ranking_global()

    def ranking_global(self):
        quizzes = models.Quiz.objects.filter(is_finished=True)
        ranking = services.get_ranking(quizzes=quizzes)
        return response.Response(ranking, status.HTTP_200_OK)

    def ranking_by_category(self, category_id):
        quizzes = models.Quiz.objects.filter(is_finished=True, category_id=category_id)
        ranking = services.get_ranking(quizzes=quizzes)
        return response.Response(ranking, status.HTTP_200_OK)
