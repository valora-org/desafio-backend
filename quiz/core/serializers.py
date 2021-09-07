from quiz.core.models import Category, Question, Result
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'category', 'question', 'answer1', 'answer2', 'answer3', 'right_answer']


class ChooseQuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']


class StartQuizSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=255)
    question = serializers.CharField(max_length=255)
    answer1 = serializers.CharField(max_length=255)
    answer2 = serializers.CharField(max_length=255)
    answer3 = serializers.CharField(max_length=255)

class ResultSerializer(serializers.Serializer):
    class Meta:
        model = Result
        fields = ['user', 'category', 'score']
        