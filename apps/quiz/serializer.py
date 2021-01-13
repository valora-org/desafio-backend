from rest_framework import serializers
from apps.quiz.models import Category, MatchGame, Selection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class MatchGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchGame
        fields = ['id', 'category_id', 'question', 'answers_one',
                  'answers_two', 'answers_three', 'correct_answers']

    def validate_correct_answers(self, value):
        if any([value == '1', value == '2', value == '3']):
            return value
        raise serializers.ValidationError('the field "correct_answers" must be a 1 to 3 string')


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'

    def validate_player_selection(self, value):
        if any([value == '1', value == '2', value == '3']):
            return value
        raise serializers.ValidationError('the field "player_selection" must be a 1 to 3 string')
