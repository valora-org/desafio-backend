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
            'id',
            'text', 
            'is_correct',
            
        ]


class QuestionSerializer(serializers.ModelSerializer):

    quiz = QuizSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True, many=True)

    class Meta:
    
        model = Question
        fields = [
            'quiz',
            'id',
            'text',
            'answer',       
        ]

    def increase_score(self):
        user_score = User.score
        if user_score >= 0:
            user_score = user_score + 1
        return user_score
    
    def decrease_score(self):
        user_score = User.score
        if user_score >= 0:
            user_score = user_score - 1
        else:
            user_score = user_score
        return user_score
    
    def validate_correct_answer(self, request):
        """
        Used to check with the player hit the correct answer
        """
        
    
