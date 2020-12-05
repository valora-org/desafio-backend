#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer, UserSerializer, GroupSerializer
from .models import Category, Question, Answer

from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

# Create your views here.

#class CategoryViewSet(viewsets.ModelViewSet):
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
    queryset = Question.objects.all().order_by('question')
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
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())
        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request):
        print(request.user.groups.filter(name="Admin").exists())
        if((request.user.groups.filter(name="Admin").exists()) == False):
            response = {'message': 'Create function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.IsAuthenticated]


