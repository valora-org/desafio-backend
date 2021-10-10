from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from random import random
from desafiobackend.quiz.models import Quiz, Category, Question, Answer, Option
        

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title',)


class QuizSerializer(ModelSerializer):
    questions = serializers.SerializerMethodField()

    def get_questions(self, obj):
        return QuestionSerializer(obj.questions.all(), many=True).data

    class Meta:
        model = Quiz
        fields = "__all__"
        extra_kwargs = {
            "category": {"required": True},
            "user": {"required": False}
        }
    
    def create(self, validated_data):
        user = self.context["request"].user
        category = validated_data.pop("category")
        # Returns 10 questions randomly
        questions = Question.objects.filter(category=category).order_by("?")[0:10]

        quiz = Quiz.objects.create(
            user=user,
            category=category
        )
        quiz.questions.add(*questions)
        quiz.save()
        return quiz


class QuestionSerializer(ModelSerializer):
    options = serializers.SerializerMethodField()

    def get_options(self, obj):
        return OptionSerializer(obj.options.all(), many=True).data
        
    class Meta:
        model = Question
        fields = ("enunciation", "options",)


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "description"]


class RankingSerializer(serializers.Serializer):
    name = serializers.CharField()
    total_points = serializers.IntegerField()

    class Meta:
        fields = "__all__"