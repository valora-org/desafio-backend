from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Question, Answer, Quiz, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class AnswerAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ('question', 'is_right')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ()


class QuestionCreateSerializer(WritableNestedModelSerializer):
    answers = AnswerAdminSerializer(source='answer_set', many=True)

    class Meta:
        model = Question
        exclude = ()


class QuestionListSerializer(WritableNestedModelSerializer):
    answers = AnswerSerializer(source='answer_set', many=True)

    class Meta:
        model = Question
        exclude = ('category',)


class QuizListSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        exclude = ('answers',)


class QuizSerializer(WritableNestedModelSerializer):
    questions = QuestionListSerializer(many=True)

    class Meta:
        model = Quiz
        exclude = ('answers',)


class QuizResultSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    answers = AnswerAdminSerializer(many=True)

    class Meta:
        model = Quiz
        exclude = ()


class GameCreateSerializer(serializers.Serializer):
    category = serializers.SlugField(required=True)
