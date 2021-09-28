import random

from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from api.models import User, Category, Answer, Question, Quiz
from api.serializers import UserSerializer, CategorySerializer, AnswerSerializer, QuestionSerializer, QuizSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['description']


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=request.data['category'])
        del request.data['category']

        questions = request.data['question']
        del request.data['question']

        for item_question in questions:
            answers = item_question['answer']
            del item_question['answer']
            question = Question(**item_question)
            question.category = category
            question.save()
            for answer in answers:
                answer_serializer = AnswerSerializer(data=answer)
                if not answer_serializer.is_valid():
                    return Response({'result': 'Bad Formatted Answer'},
                                    status=status.HTTP_400_BAD_REQUEST)
                ans = answer_serializer.save()
                question.answer.add(ans)
        return Response('ok')


class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, **kwargs):
        queryset = Question.objects.filter(category__id=request.data['category'])
        if not queryset:
            return Response({"detail": "Category not found"},
                            status=status.HTTP_404_NOT_FOUND)
        questions = list(queryset)
        random.shuffle(questions)

        quiz = Quiz()
        quiz.user = get_object_or_404(User, id=request.data['user'])
        quiz.category = get_object_or_404(Category, id=request.data['category'])
        quiz.save()
        quiz.questions.set(questions[:5])
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        quiz = self.get_object()
        quiz_id = kwargs['pk']
        question_id = request.data['question']
        answer_id = request.data['answer']
        try:
            question = Question.objects.get(id=question_id, quiz__id=quiz_id)
            ans = Answer.objects.get(pk=answer_id, question__id=question.id)
            if ans.is_right:
                quiz.correct_answers += 1
                quiz.save()
            else:
                if quiz.correct_answers > 0:
                    quiz.correct_answers -= 1
                    quiz.save()
        except Exception as e:
            return Response({"detail": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response("Ok", status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def finish(self, request, pk):
        quiz = get_object_or_404(Quiz, id=pk)

        score_user = Quiz.objects.filter(user=quiz.user.pk).aggregate(Sum('correct_answers'))
        ranking = Quiz.objects.all().values('user').annotate(Sum('correct_answers'))

        user_position = [index for index, item in enumerate(ranking) if item['user'] == quiz.user.id]
        quiz.save()  # Atualiza o camp  o 'finish' com o datetime atual

        data = {
            'score': quiz.correct_answers,
            'score_global': score_user['correct_answers__sum'],
            'user_id': quiz.user.id,
            'user_email': quiz.user.email,
            'ranking_position': user_position[0] + 1
        }
        return Response(data, status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='ranking-global')
    def ranking_global(self, request):
        ranking = Quiz.objects.all().values('user',
                                            'user__email') \
            .annotate(ranking=Sum('correct_answers')) \
            .order_by('-ranking')

        data = [{"user_id": item['user'],
                 "user_email": item["user__email"],
                 "user_score": item["ranking"]}
                for item in ranking]
        return Response(data)

    @action(methods=['get'], detail=False, url_path='ranking-by-category')
    def ranking_by_category(self, request):
        ranking_by_cat = Quiz.objects.all().values('category',
                                                   'category__description') \
            .annotate(ranking=Sum('correct_answers')) \
            .order_by('-ranking')

        data = [{"description": item["category__description"],
                 "score": item["ranking"]}
                for item in ranking_by_cat]

        return Response(data)
