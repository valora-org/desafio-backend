from django.db.models import fields
from rest_framework import serializers

from .models import (
    CategoryModel, AnswerModel, QuestionModel, CategoryQuestionModel,
    RankingModel
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        write_only_fields = ('id',)
        fields = (
            'id',
            'name'
        )

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionModel
        fields = (
            'id',
            'question'
        )


class CategoryQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryQuestionModel
        fields = (
            'id',
            'category',
            'question'
        )


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnswerModel
        fields = (
            'id',
            'question',
            'answer',
            'correct_answer',
        )

class RankingSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    category_name = serializers.SerializerMethodField('get_category_name')
    class Meta:
        model = RankingModel
        fields = (
            'username',
            'category_name',
            'value'
        )
    
    def get_username(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    
    def get_category_name(self, obj):
        return f'{(obj.category.name).upper()}'


class QuizSerializer(serializers.Serializer):

    id_question = serializers.UUIDField(required=True)
    id_answer = serializers.UUIDField(required=True)

