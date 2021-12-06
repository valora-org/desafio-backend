from attr import fields
from rest_framework import serializers

from quizzes.models import Answer, Question, Ranking


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("text", "id")


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = "__all__"
