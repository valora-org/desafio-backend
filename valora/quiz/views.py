from rest_framework import permissions
from rest_framework.decorators import api_view

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.http import Http404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

from .models import Category, Answer, Question, Classification
from .serializers import CategorySerializer, QuestionSerializer
from .serializers import AnswerSerializers


class CategoryList(generics.ListCreateAPIView):
    """
    List all categories
    """
    permission_classes = (permissions.DjangoModelPermissions,)
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
    @user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
    def post(request):
        if not request.user.groups.filter(name="Admin").exists():
            response = {'error': 'POST not allowed for this user.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

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
    @user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
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
def get_ranking(request, _id=None):
    if _id is None:
        clas = Classification.objects.all().order_by('category')
    else:
        clas = Classification.objects.filter(category_id=_id)

    dic = {}
    for c in clas:
        if c.author not in dic:
            dic[c.author.username] = 0
        dic[c.author.username] += c.points

    response = dict(sorted(dic.items(), key=lambda item: item[1]))
    return Response(response, status=status.HTTP_200_OK)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
     Each new user that is created is added to the Player group
    """
    if created:
        is_superuser = instance.is_superuser
        if not is_superuser:
            instance.groups.add(Group.objects.get(name='Player'))
