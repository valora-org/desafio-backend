from rest_framework.serializers import ModelSerializer

from api.models import User, Category, Answer, Question, Quiz, Play


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'is_active', 'is_admin')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ('id', 'name', 'category', 'question')


class PlaySerializer(ModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'
