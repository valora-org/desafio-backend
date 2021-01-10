from django.shortcuts import redirect
from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from quiz.models import Category, Question
from quiz.serializer import CategorySerializer, QuestionAdminSerializer, QuestionSerializer
from user.models import UserProfile


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('-category')
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class CategoryAdminViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-category')
    serializer_class = CategorySerializer
    filterset_fields = ['category']
    permission_classes = (permissions.IsAdminUser,)


class QuestionAdminViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-category')
    serializer_class = QuestionAdminSerializer
    filterset_fields = ['category']
    permission_classes = (permissions.IsAdminUser,)


class StartQuiz(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "form.html"
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self, category_id):
        profile = UserProfile.objects.get(user=self.request.user)
        queryset = Question.objects.filter(category__id=category_id).exclude(
            question__in=[item.question for item in profile.question_correct.all()]).exclude(
            question__in=[item.question for item in profile.question_wrong.all()]).order_by('?')[0:10]
        return queryset

    def get(self, request, category_id):
        serializer = QuestionSerializer(self.get_queryset(category_id), many=True)
        return Response(serializer.data)

    def post(self, request, category_id):
        profile_user = UserProfile.objects.get(user=request.user)
        temp_points = 0
        for dict_ in self.request.data:
            question = Question.objects.filter(category_id=category_id, question=dict_['question'])[0]
            if question.correct == dict_['correct_user']:
                profile_user.adicionar_points()
                profile_user.question_correct.add(question)
                temp_points += 1
            else:
                temp_points -= 1
                profile_user.remove_points()
                profile_user.question_wrong.add(question)

        profile_user.temp_points = UserProfile.negativos_pontos(soma=temp_points)
        profile_user.save()
        return redirect('user:temp_points')
