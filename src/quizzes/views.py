from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from quizzes.mixins import QuizPlayViewMixin, QuizCreationViewMixin
from quizzes.utils import Quizzes
from quizzes import serializers
from quizzes import serializers


class GetQuiz(QuizPlayViewMixin):
    
    serializer_class = serializers.GetQuizSerializer

    def post(self, request):
        category = request.data.get('category')
        user = request.user
        if not user.current_quiz:
            user.set_current_quiz(Quizzes(category=category).base_quiz)
        
        random_user_question = user.get_random_question_from_current_quiz()
        return Response({
            "Pergunta": random_user_question.question_text,
            "Alternativa (1)": random_user_question.first_choice,
            "Alternativa (2)": random_user_question.second_choice,
            "Alternativa (3)": random_user_question.third_choice,
            })

class PlayQuiz(QuizPlayViewMixin):
    
    serializer_class = serializers.PlayQuizSerializer
    
    def post(self, request):
        user = request.user
        response_data = {}
        
        if not user.current_quiz:
            return Response({"Permissão Negada":"Primeiro você deve obter um Quizz para seu usuário!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.is_the_last_question():
            response_data[f"Posição no Ranking global"] = user.position_in_global_ranking()
        
        current_question = user.get_current_question_from_quiz()
        answer_choice = request.data.get("answer_choice")
        
        if  answer_choice == current_question.correct_choice:
            num_question = user.exclude_current_question_and_increase_ranking_point()
            response_data['response'] = f"Parabéns *{num_question}"
        else: 
            num_question = user.exclude_current_question_and_decrease_ranking_point()
            response_data['response'] = f"Que pena {user} você errou a questão!, volte no endpoint de obtenção de Quiz para pegar a próxima questão. Não se preocupe seu Quiz atual não será apagado enquanto você não responder todas as questões! *{num_question}"
        
        return Response(response_data)


class CreateQuestion(QuizCreationViewMixin):
    
    serializer_class = serializers.QuestionSerializer


class CreateCategory(QuizCreationViewMixin):
    
    serializer_class = serializers.CategorySerializer
        