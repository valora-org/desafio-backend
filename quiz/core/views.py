from quiz.core.models import Category, Question
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from quiz.core.serializers import (CategorySerializer, 
                                   QuestionSerializer, 
                                   ChooseQuizSerializer
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
    permission_classes = [permissions.IsAdminUser]
    