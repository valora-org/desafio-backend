from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (
    CategoryModel, AnswerModel, QuestionModel, CategoryQuestionModel,
    RankingModel
)

UserModel = get_user_model()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_admin = serializers.BooleanField(write_only=True, required=True)

    def create(self, validated_data):
        admin = validated_data['is_admin']
        data = {
            'username': validated_data['username'],
            'email': validated_data['email'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'is_staff': admin,
        }
        user = UserModel.objects.create(**data)
        user.set_password(validated_data['password'])
        
        if admin is True:
            user.is_superuser = True
        user.save()
        return user

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

