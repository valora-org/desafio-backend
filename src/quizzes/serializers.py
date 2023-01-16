from rest_framework import serializers
from quizzes import models

class GetQuizSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=100)


class PlayQuizSerializer(serializers.Serializer):
    choices = (
        ("first_choice", "Primeira escolha"),
        ("second_choice", "Segunda escolha"),
        ("third_choice", "Terceira escolha")
    )
    answer_choice = serializers.ChoiceField(choices=choices)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'