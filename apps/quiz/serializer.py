from rest_framework import serializers
from apps.quiz.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'question', 'answers_one', 'answers_two',
                  'answers_three', 'correct_option', 'player_response']
