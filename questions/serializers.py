from rest_framework import serializers

from answers.models import Answer
from questions.models import Question


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'answer',
            'is_correct',
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'level',
            'created_at',
            'is_active',
            'quiz',
        )


class SmallestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question',)


class DetailedQuestionSerializer(serializers.ModelSerializer):
    answers = QuestionAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'level',
            'created_at',
            'is_active',
            'quiz',
            'answers',
        )


class LessDetailedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'level',
            'is_active',
            'created_at',
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',
            'is_correct',
            'question',
        )


class DetailedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',
            'is_correct',
        )
