from quiz import models
from rest_framework import viewsets
from rest_framework import permissions
from quiz.api import serializers
from rest_framework.filters import SearchFilter
from django.core.exceptions import PermissionDenied
import random


# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer
#     filter_backends =  (SearchFilter,)
#     filter_fields = ('id', 'role', 'username', 'score')
#     search_fields = ('role', 'username', 'score')

class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    filter_backends =  (SearchFilter,)
    filter_fields = ('id', 'user', 'category')
    search_fields = ('user', 'category')

    # def list(self, request, *args, **kwargs):
    #     if request.user.role:
    #         return super().list(request, *args, **kwargs)
    #     else:
    #         print(request)
    #         print(dir(request))
    #         return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if request.user.role:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    def update(self, request, *args, **kwargs):
        if request.user.role:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user.role:
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

    # def list(self, request, *args, **kwargs):
    #     if request.user.role:
    #         return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        limit_questions = models.Quiz.objects.get(id=request.data['quiz']).question_set.count() <= 10
        
        if request.user.role and limit_questions:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    def update(self, request, *args, **kwargs):
        if request.user.role:
            return super().update(request, *args, **kwargs)
        elif request.PUT.get('user_answer') and request.user.score < 10:
            try:
                user_answer = request.PUT.get('user_answer')
                current_question = models.Question.objects.get(id=kwargs['pk'])

                # TODO: O player pode alterar mais de um campo na mesma requisição.
                if user_answer == current_question.correct_answer:
                    request.user.score += 1
                else:
                    request.user.score -= 1
            except:
                pass
            
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        
    def destroy(self, request, *args, **kwargs):
        if request.user.role:
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

    # def list(self, request, *args, **kwargs):
    #     if request.user.role:
    #         return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        limit_answers = models.Quiz.objects.get(id=request.data['quiz']).question_set.count() <= 3
        
        if request.user.role and limit_answers:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    
    def update(self, request, *args, **kwargs):
        if not request.user.role:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user.role:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()