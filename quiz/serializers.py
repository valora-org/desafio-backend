from rest_framework import serializers
from quiz.models import Question, Answer, Quiz
from accounts.models import CustomUser as User



class QuizSerializer(serializers.ModelSerializer):

    
    
    class Meta:
        model = Quiz
        fields = [
            'url',
            'name', 
            'category',
            
        ]


class AnswerSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Answer
        fields = [
            'question',
            'id',
            'text', 
            'is_correct',
            
        ]


class QuestionSerializer(serializers.ModelSerializer):

    
    answer = AnswerSerializer(read_only=True, many=True)

    class Meta:
    
        model = Question
        fields = [
            'url',
            'id',
            'quiz',
            'text',
            'answer',       
        ]


class RankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'score'
        ]
        
    
