from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from questions.models import Category, Question


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    category = SerializerMethodField()
    correct_answer = SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_correct_answer(self, obj):
        return obj.get_correct_answer_display()

    def get_category(self, obj):
        return obj.category.name


class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "question",
            "first_answer",
            "second_answer",
            "third_answer",
        ]
