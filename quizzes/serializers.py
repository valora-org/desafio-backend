from rest_framework import serializers

from answers.serializers import AnswerSerializer
from questions.models import Question
from quizzes.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
        )


class RandomQuizQuestionsSerializer(serializers.ModelSerializer):
    # answers = serializers.StringRelatedField(many=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'question',
            'answers',
        )
