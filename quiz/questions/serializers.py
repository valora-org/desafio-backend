from rest_framework import serializers

from quiz.categories.models import Category

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Question serializer."""

    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        required=True,
        queryset=Category.objects.all(),
        allow_empty=False)

    class Meta:
        """Meta info for question serializer."""

        model = Question
        fields = [
            'id', 'categories', 'statement', 'choices', 'correct_choice_index'
        ]
        depth = 1
