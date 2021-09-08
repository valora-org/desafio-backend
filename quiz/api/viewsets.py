from quiz import models
from rest_framework import viewsets
from rest_framework import permissions
from quiz.api import serializers
from rest_framework.filters import SearchFilter
from django.core.exceptions import PermissionDenied
import random


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserSerializer
    filter_backends =  (SearchFilter,)
    filter_fields = ('id', 'username', 'admin')
    search_fields = ('username', 'admin')
    queryset = models.User.objects.all()

class RankingViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.RankingSerializer
    filter_backends =  (SearchFilter,)
    filter_fields = ('id', 'username', 'score')
    search_fields = ('username', 'score')
    queryset = models.User.objects.filter(admin=False)

class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.QuizSerializer
    queryset = models.Quiz.objects.all()
    filter_backends =  (SearchFilter,)
    filter_fields = ('id', 'user', 'category')
    search_fields = ('user', 'category')
    
    def create(self, request, *args, **kwargs):
        if request.user.admin:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    def update(self, request, *args, **kwargs):
        if request.user.admin:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user.admin:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied()

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    filter_fields = ('id', 'quiz', 'question', 'user_answer', 'correct_answer')
    filter_backends =  (SearchFilter,)
    search_fields = ('quiz', 'question', 'user_answer', 'correct_answer')
    
    def create(self, request, *args, **kwargs):
        limit_questions = models.Quiz.objects.get(id=request.data['quiz']).question_set.count() < 10
        
        if request.user.admin and limit_questions:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    def update(self, request, *args, **kwargs):
        user = models.User.objects.get(id=request.user.id)

        if request.user.admin:
            return super().update(request, *args, **kwargs)
        elif request.POST.get('user_answer') and user.score < 10:
            user_answer = request.POST.get('user_answer')
            current_question = models.Question.objects.get(id=kwargs['pk'])

            if int(user_answer) == int(current_question.correct_answer):
                user.score += 1
            elif user.score > 0:
                user.score -= 1

            user.save()

            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        
    def destroy(self, request, *args, **kwargs):
        if request.user.admin:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    filter_fields = ('id', 'question', 'answer')
    filter_backends =  (SearchFilter,)
    search_fields = ('question', 'answer')
    
    def create(self, request, *args, **kwargs):
        limit_answers = models.Question.objects.get(id=request.data['question']).answer_set.count() < 3
        
        if request.user.admin and limit_answers:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    def update(self, request, *args, **kwargs):
        if not request.user.admin:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user.admin:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()