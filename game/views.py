#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer, UserSerializer, GroupSerializer, QuizPageSerializer, QuizSerializer
from .models import Category, Question, Answer, QuizPage, Quiz

from django.contrib.auth.models import User, Group
from rest_framework import permissions 

from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('category')
    serializer_class = CategorySerializer
    
    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())
        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    permission_classes = [permissions.IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('category')
    serializer_class = QuestionSerializer

    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())
        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.IsAuthenticated]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('question')
    serializer_class = AnswerSerializer

    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())
        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    permission_classes = [permissions.IsAuthenticated]

class QuizPageViewSet(viewsets.ModelViewSet):
    
    queryset = QuizPage.objects.all()
    serializer_class = QuizPageSerializer

    def list(self, request):
        queryset = QuizPage.objects.all()

        serializer = QuizPageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())

        if request.method=='PUT' and not override_method: 
            print('This is a PUT')
        return

        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = QuizPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        print('inside put')
        return self.update(request, *args, **kwargs)

    permission_classes = [permissions.IsAuthenticated]


class QuizViewSet(viewsets.ModelViewSet):
    
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def list(self, request):
        queryset = Quiz.objects.all()
        #print(queryset[0].points) ranking filter where user == current
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())
        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.IsAuthenticated]




