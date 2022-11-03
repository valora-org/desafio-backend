from rest_framework import serializers

from .models import Answer, Question, Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
        )


class AleatoryQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'answers',
        )
