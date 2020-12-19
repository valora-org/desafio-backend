
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view


from django.http import Http404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group

from .models import Category, Answer, Question, Classification
from .serializers import CategorySerializer, QuestionSerializer
from .serializers import AnswerSerializers, ClassificationSerializers


class CategoryList(generics.ListCreateAPIView):
    """
    List all categories
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class CategoryDetail(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionList(generics.ListCreateAPIView):
    """
    List all questions
    """
    queryset = Question.objects.all().order_by('category')
    serializer_class = QuestionSerializer


@api_view(['GET'])
def get_question_list_by_category(request, _id):
    questions = Question.objects.filter(category_id=_id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionDetail(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerList(generics.ListCreateAPIView):
    """
    List all answers
    """
    queryset = Answer.objects.all().order_by('category')
    serializer_class = AnswerSerializers


class AnswerViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return self.queryset

    def create(self, request, *args, **kwargs):
        try:
            serializer = AnswerSerializers
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            print(e.args)
            response = {'msg': e.args}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_answer_list_by_category(request, _id):
    answer = Answer.objects.filter(category_id=_id)
    serializer = AnswerSerializers(answer, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_answer_list_by_user(request, _id):
    answer = Answer.objects.filter(author_id=_id)
    serializer = AnswerSerializers(answer, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_overall_ranking(request):
    c = Classification.objects.all().order_by('-points')
    serializer = ClassificationSerializers(c, many=True)

    response={}


    return Response(serializer.data, status=status.HTTP_200_OK)


