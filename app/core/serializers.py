from django.db.models import fields
from rest_framework import serializers

from .models import CategoryModel, AnswerModel, QuestionModel


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = (
            'id',
            'name'
        )

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnswerModel
        fields = (
            'id',
            'category',
            'answer'
        )

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionModel
        fields = (
            'id',
            'category',
            'answer'
        )