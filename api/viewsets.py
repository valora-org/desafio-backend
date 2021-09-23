from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from api.models import User, Category, Answer, Question, Quiz, Play
from api.serializers import UserSerializer, CategorySerializer, AnswerSerializer, QuestionSerializer, QuizSerializer, \
    PlaySerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=request.data['category'])
        del request.data['category']

        questions = request.data['question']
        del request.data['question']

        quiz = Quiz(**request.data, category=category)
        quiz.save()

        for item_question in questions:
            answers = item_question['answer']
            del item_question['answer']
            question = Question(**item_question)
            question.save()
            for answer in answers:
                answer_serializer = AnswerSerializer(data=answer)
                if not answer_serializer.is_valid():
                    return Response({'result': 'Bad Formatted Answer'},
                                    status=status.HTTP_400_BAD_REQUEST)
                ans = answer_serializer.save()
                question.answer.add(ans)
            quiz.question.add(question)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
