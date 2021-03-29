from rest_framework.generics import (ListAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     )
from .serializers import (QuizCreateSerializer,
                          QuizListRetrieveSerializer,
                          CategoryCreateSerializer,
                          StartQuizSerializer,
                          QuizUpdateSerializer,
                          FinishQuizSerializer,)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Quiz, Category
import random


class RegisterCategoryView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = CategoryCreateSerializer

    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterQuizView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = QuizCreateSerializer

    def post(self, request):
        serializer = QuizCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListQuizView(ListAPIView):

    serializer_class = QuizListRetrieveSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Quiz.objects.all()


class RetrieveQuizView(RetrieveAPIView):

    serializer_class = QuizListRetrieveSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

    def get_queryset(self):
        return Quiz.objects.filter(id=self.kwargs['id'])


class StartQuizView(RetrieveAPIView):
    serializer_class = StartQuizSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "category"

    def retrieve(self, request, *args, **kwargs):
        try:
            quiz_object = Quiz.objects.get(category=self.kwargs['category'])
            questions = list(quiz_object.question.values())
            random_questions = random.sample(questions, 10)
            for row in random_questions:
                row.pop('correct_letter')
        except Quiz.DoesNotExist:
            return Response({"Error": "Category not Found"}, status.HTTP_400_BAD_REQUEST)

        return Response({
            'id': quiz_object.id,
            'title': quiz_object.title,
            'category': quiz_object.category.id,
            'question': random_questions
        })


class DeleteQuizView(DestroyAPIView):
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Quiz.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class UpdateQuizView(UpdateAPIView):
    serializer_class = QuizUpdateSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Quiz.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()


class UpdateCategoryView(UpdateAPIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Category.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()


class DeleteCategoryView(DestroyAPIView):
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = Category.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        instance.delete()


class FinishQuizView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FinishQuizSerializer

    def post(self, request):
        serializer = FinishQuizSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
