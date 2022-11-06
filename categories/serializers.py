from rest_framework import serializers

from categories.models import Category
from core.exceptions import UniqueException
from questions.models import Question
from questions.serializers import (
    LessDetailedQuestionSerializer,
    QuestionAnswerSerializer,
    SmallestQuestionSerializer,
)
from quizzes.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'name',
            'id',
            'created_at',
        )

        read_only_fields = ('id',)

    def validate_name(self, name: str):
        return name.title()


class LessDetailedQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'name',
            'id',
            'created_at',
            'category',
        )

        read_only_fields = (
            'id',
            'created_at',
        )

    def validate_name(self, name: str):
        return name.title()


class DetailedQuizSerializer(serializers.ModelSerializer):
    questions = SmallestQuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = (
            'name',
            'id',
            'created_at',
            'category',
            'questions',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

    read_only_fields = ('id',)

    def validate_name(self, name: str):
        name_exists = Category.objects.filter(name=name.title()).exists()
        if name_exists:
            raise UniqueException({'detail': 'category already exists'})

        return name.title()


class DetailedCategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quizzes',
        )


class RandomQuestionsQuizSerializer(serializers.ModelSerializer):
    # answers = serializers.StringRelatedField(many=True)
    answers = QuestionAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'question',
            'answers',
        )
