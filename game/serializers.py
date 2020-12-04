from rest_framework import serializers

from django.contrib.auth.models import User, Group

from .models import Category, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id','title')

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'question','category')

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'isCorrect','question')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']