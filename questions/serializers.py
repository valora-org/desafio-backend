from rest_framework import serializers

from answers.models import Answer
from questions.models import Question


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = QuestionAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'question',
            'answers',
        )


class DetailedQuestionSerializer(serializers.ModelSerializer):
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

        read_only_fields = (
            'id',
            'created_at',
        )


class LessDetailedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'level',
            'is_active',
        )

        read_only_fields = ('id',)


class DetailedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',
            'is_correct',
        )

        read_only_fields = ('id',)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',
            'is_correct',
            'question',
        )

        read_only_fields = ('id',)
