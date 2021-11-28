from django.forms.widgets import TextInput
from rest_framework import serializers 
from quiz.models.question import *

class OptionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option 
        fields = ['text']

class QuestionGetSimpleSerializer(serializers.ModelSerializer):
    options = OptionSimpleSerializer(many=True)
    class Meta:
        model = Question 
        fields = ["enunciation","options"]