from rest_framework import serializers 
from quiz.models.quiz import *

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz 
        fields = "__all__"