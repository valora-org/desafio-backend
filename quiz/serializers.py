from rest_framework import serializers
from quiz.models import Question, Answer, Quiz
from accounts.models import CustomUser as User



class QuizSerializer(serializers.ModelSerializer):

    
    
    class Meta:
        model = Quiz
        fields = [
            'url',
            'name',        
        ]


class AnswerSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Answer
        fields = [
            
            'id',
            'question',
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
            'category',
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
        
    
