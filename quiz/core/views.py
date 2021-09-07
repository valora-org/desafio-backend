from quiz.core.models import Category, Question, Result
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from quiz.core.serializers import (CategorySerializer, 
                                   QuestionSerializer, 
                                   ChooseQuizSerializer,
                                   StartQuizSerializer,
                                   )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class ChooseQuizViewSet(viewsets.ModelViewSet):
    def categories_with_10_questions():
        choosed = []
        for category in Category.objects.all():
            try:
                if len(Question.objects.filter(category=category)) >= 10:
                    choosed.append(category.id)
            except:
                print(f'Category {category.category} have less than 10 questions')
        return Category.objects.filter(pk__in=choosed)
    queryset = categories_with_10_questions()
    serializer_class = ChooseQuizSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class StartQuizViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        pass

    def retrieve(self, request, pk):
        category = Category.objects.get(pk=pk)
        queryset = Question.objects.filter(category=category)[:10]
        serializer = StartQuizSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = StartQuizSerializer


def calculate_score(request):
    answers = request.data['answers']
    score = 0
    for question, answer in answers.items():
        rigth_answer = Question.objects.get(id=int(question)).right_answer
        if answer == rigth_answer:
            score += 1
        else:
            score -= 1
    if score < 0:
        return 0
    return score

def save_quiz_result(user, category, score):
    obj = Result(user=user, category=category, score=score)
    obj.save()

from django.db.models import F, Window, Count
from django.db.models.functions import Rank

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resultList(request):
    user = request.user
    category_id = request.data['category']
    category = Category.objects.get(id=category_id)
    score = calculate_score(request)
    category_score = Result.objects.filter(category=category).filter(user=user).aggregate(Sum('score'))
    global_score = Result.objects.filter(user=user).aggregate(Sum('score'))

    save_quiz_result(user, category, score)
    return Response({'user': user.username, 
                     'game score':score, 
                     'category':category_id, 
                     'global score': global_score['score__sum'],
                     'category score': category_score['score__sum'],
                     })