from rest_framework import viewsets, permissions
from rest_framework.response import Response
from quiz.models import Quiz, Question, Answer
from quiz.serializers import QuizSerializer, QuestionSerializer
from django.core.exceptions import PermissionDenied


   
class QuizView(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, format=None, pk=None):
        """
        Return one random question when quiz are called
        """
        question = Question.objects.filter(quiz__pk=pk).order_by('?')[:1]
        serializer = QuestionSerializer(question, context={'request': request}, many=True)
        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        
    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        
    def destroy(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    