from rest_framework import serializers
from quiz.models import Question, Answer, Quiz


class QuizSerializer(serializers.ModelSerializer):

    
    category = serializers.StringRelatedField(read_only=True)
    
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
            'question',
            'text',
            'is_correct',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    quiz = QuizSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'quiz',
            'text',
            'answer',       
        ]

    def hit_correct_answer(self):
        """
        Used to check with the player hit the correct answer
        """
        pass
