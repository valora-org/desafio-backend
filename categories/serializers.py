from rest_framework import serializers

from core.exceptions import UniqueException
from categories.models import Category
from quizzes.serializers import QuizSerializer


class CategorySerializer(serializers.ModelSerializer):
    # quizzes = QuizSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            # 'quizzes',
        )

    read_only_fields = 'id'

    def validate_name(self, name: str):
        name_exists = Category.objects.filter(name=name.title()).exists()
        if name_exists:
            raise UniqueException({'detail': 'category already exists'})

        return name.title()
