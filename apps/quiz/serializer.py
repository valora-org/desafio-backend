from rest_framework import serializers
from apps.quiz.models import Category, Match, Selection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'id_category', 'question', 'answers_one',
                  'answers_two', 'answers_three', 'correct_answers']


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
