from rest_framework import serializers
from .models import Category, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id','title')

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'question','category')

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'isCorrect','question')