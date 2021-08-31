from rest_framework import serializers

from quiz import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        read_only_fields = ("id",)
        fields = [
            "id",
            "title",
        ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        read_only_fields = ("id",)
        fields = [
            "id",
            "label",
            "category",
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        read_only_fields = ("id",)
        fields = [
            "id",
            "label",
            "question",
            "is_right",
        ]
