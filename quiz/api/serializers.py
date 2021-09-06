from quiz import models
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ['user', 'score', 'category']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ['question', 'answer']