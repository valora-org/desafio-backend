import random
import logging
from uuid import UUID

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.contrib.auth import get_user_model

from .permissions import PlayerPermission

from .models import (
    CategoryQuestionModel, AnswerModel, CategoryModel, QuestionModel,
    RankingModel
)
from .serializers import (
    CategoryQuestionSerializer, AnswerSerializer, CategorySerializer,
    QuestionSerializer, QuizSerializer, RankingSerializer, UserSerializer
)

class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    UserModel = get_user_model()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        PlayerPermission,
    )

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser]

class CategoryQuestionViewSet(viewsets.ModelViewSet):
    queryset = CategoryQuestionModel.objects.all()
    serializer_class = CategoryQuestionSerializer
    permission_classes = [IsAdminUser]


class RankingViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = RankingModel.objects.all().order_by('-value')
    serializer_class = RankingSerializer
    permission_classes = [PlayerPermission]
    
    # Neste caso, pk eh o id da category.
    def retrieve(self, request, pk):
        ranking = (
            RankingModel.objects.filter(category_id__in=[pk]).order_by('-value')
        )
        serializer = RankingSerializer(ranking, many=True)
        return Response(serializer.data)
        

class QuizAPIView(APIView):
    permission_classes = [PlayerPermission]
    def get(self, requests, category_id):
        cursor = connection.cursor()
        query = f'SELECT B.id, B.question FROM  core_categoryquestionmodel as A INNER JOIN core_questionmodel as B ON B.id = A.question_id WHERE A.category_id="{category_id.replace("-","")}";'
        cursor.execute(query)
        questions_db = cursor.fetchall()
        questions = [
            {'id': UUID(x), 'question': y} for x, y in questions_db
        ]
        random.shuffle(questions)
        answers_db = AnswerModel.objects.all()
        answers = list(answers_db.values())
        list_quiz = []
        for question in questions:
            random.shuffle(answers)
            question_answers_true = list(
                filter(
                    lambda x: (
                        x['question_id'] == question['id']
                        and x['correct_answer'] is True
                    ),
                    answers
                )
            )[0:1]
            question_answers_false = list(
                filter(
                    lambda x: (
                        x['question_id'] == question['id']
                        and x['correct_answer'] is False
                    ),
                    answers
                )
            )[0:2]
            list_questions = question_answers_true + question_answers_false
            random.shuffle(list_questions)
            data = {
                'question': {
                    'id':question['id'],
                    'question': question['question']
                },
                'answers': [
                    {'id': x['id'], 'answer': x['answer']}
                    for x in list_questions
                ]
            }
            list_quiz.append(data)
        # Verifica se o quiz possui >= 10 perguntas.
        if len(list_quiz) >= 10:
            return Response(list_quiz[0:10], status.HTTP_200_OK)
        else:
            result = {
                'msg': 'Quiz ainda não possui perguntas sufucientes.'
            }
            return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, requests, category_id):
        user = requests.user
        result = {}
        serialize_quiz = QuizSerializer(data=requests.data, many=True)
        if serialize_quiz.is_valid(raise_exception=True):
            list_answers = list(
                {x['id_answer'] for x in serialize_quiz.validated_data}
            )
            list_answers_db = list(
                AnswerModel.objects.filter(id__in=list_answers).values()
            )
            list_correct_answers = list(filter(
                lambda x: x['correct_answer'] == True, list_answers_db
            ))
            category = CategoryModel.objects.get(id=category_id)
            data = {
                'user_id': user.id,
                'category_id': category.id,
                'value': len(list_correct_answers)
            }
            #Cria ou atualiza os dados do ranking
            try:
                ranking = RankingModel.objects.get(
                    category=category_id,
                    user=user.id
                )
                ranking.value = data['value']
                ranking.save()
            except ObjectDoesNotExist:
                RankingModel.objects.create(**data)
            global_ranking = list(
                RankingModel.objects.all().order_by('-value').values()
            )
            index_user = [
                i for i, _ in enumerate(global_ranking)
                if _['user_id'] == user.id
            ][0]
            result = {
                'punctuation': data['value'],
                'ranking_position': index_user + 1
            }
            return Response(
                result, status=status.HTTP_201_CREATED
            )
        else:
            logging.error(msg='Erro ao processar os dados')
            return Response({'Result': result}, status.HTTP_200_OK)
