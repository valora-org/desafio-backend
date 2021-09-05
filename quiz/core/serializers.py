from quiz.core.models import Category, Question
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
