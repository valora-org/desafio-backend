from rest_framework import serializers

from django.contrib.auth.models import User, Group

from .models import Category, Question, Answer, QuizPage, Quiz

class CategorySerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('id','category','questions')

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(read_only=True,many=True)
    category = serializers.SlugRelatedField(slug_field="category", queryset=Category.objects.all())
    class Meta:
        model = Question
        fields = ('id', 'question','category','answers')

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field="question", queryset=Question.objects.all())
    class Meta:
        model = Answer
        fields = ('id', 'answer', 'isCorrect','question')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class QuizPageSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer()
    question = serializers.SlugRelatedField(slug_field="question", queryset=Question.objects.all())
    quiz = serializers.SlugRelatedField(slug_field="title", queryset=Quiz.objects.all())
    class Meta:
        model = QuizPage
        fields = ['id','question', 'quiz']

class QuizSerializer(serializers.ModelSerializer):
    points = serializers.StringRelatedField(read_only=True)
    vote = serializers.StringRelatedField(read_only=True)
    #quiz_page = serializers.StringRelatedField(read_only=True,many=True)
    
    class Meta:
        model = Quiz
        fields = ['id','points','title','vote']