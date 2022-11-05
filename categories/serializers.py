from rest_framework import serializers

from categories.models import Category
from core.exceptions import UniqueException
from questions.models import Question
from questions.serializers import QuestionAnswerSerializer
from quizzes.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
        )


class CategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quizzes',
        )

    read_only_fields = ('id',)

    def validate_name(self, name: str):
        name_exists = Category.objects.filter(name=name.title()).exists()
        if name_exists:
            raise UniqueException({'detail': 'category already exists'})

        return name.title()


class DetailedQuizSerialized(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
            'created_at',
            'category',
        )

        read_only_fields = (
            'id',
            'created_at',
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
