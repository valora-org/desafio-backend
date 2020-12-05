from rest_framework import serializers

from django.contrib.auth.models import User, Group

from .models import Category, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('id','category','questions')

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Question
        fields = ('id', 'question','category','answers')

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ('id', 'answer', 'isCorrect','question')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #groups = serializers.ManyRelatedField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']