from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django.db.models.expressions import Exists, OuterRef, Subquery
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer, RankingSerializer
from ..models import Category, Question, Quiz, Answer, Option
from rest_framework import mixins
from django.db.models import F, Case, Value, When, Count
from django.db.models.functions import Coalesce
# import permission
from permissions import *


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminPermission]
    queryset = Question.objects.all()
    
    @action(methods=['post'], detail=True)
    def create_option(self, request, pk=None):
        question = get_object_or_404(Question, pk=pk)
        Option.objects.create(**request.data, question=question)
        return Response({"Options created!"}, status=status.HTTP_201_CREATED)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsPlayerPermission,)
    queryset = Category.objects.all()


class QuizViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = (IsPlayerPermission,)
    
    @action(methods=['post'], detail=True)
    def answer(self, request, pk=None):
        quiz = get_object_or_404(Quiz, pk=pk, user=self.request.user, is_finished=False)
        data = request.data
        if not "id_option" in data:
            raise serializers.ValidationError({'id_option': 'required'})

        option = get_object_or_404(Option, pk=data["id_option"])

        questions = quiz.questions.all()

        if not questions.filter(options=option).exists():
            raise serializers.ValidationError({'id_option': 'is not present for self quiz'})
            
        Answer.objects.get_or_create(quiz=quiz, option=option)
        
        return Response({"Question is answered!"}, status=status.HTTP_201_CREATED)
    
    
    @action(methods=['post'], detail=True)
    def finish(self, request, pk=None):
        permission_classes = [IsPlayerPermission]
        quiz = get_object_or_404(Quiz, pk=pk, user=self.request.user, is_finished=False)
        quiz.is_finished = True
        quiz.save()

        sub_accepteds = Answer.objects.filter(
            option__is_correct=True,
            quiz__user=OuterRef("pk")
        ).values("quiz__user_id").annotate(count=Count("*"))

        sub_faults = Answer.objects.filter(
            option__is_correct=False,
            quiz__user=OuterRef("pk")
        ).values("quiz__user_id").annotate(count=Count("*"))
        
        ranking = User.objects.filter(
            quiz__is_finished=True
        ).annotate(
            accepteds=Subquery(sub_accepteds.values("count")),
            faults=Subquery(sub_faults.values("count")),
        ).annotate(
            points=F("accepteds")-F("faults")
        ).annotate(
            total_points=Case(
                When(points__lt=0, then=Value(0)),
                default=F('points')
            )
        ).values("first_name", "total_points").order_by("-total_points")
        
        return Response(ranking, status=status.HTTP_200_OK) 
        

    def retrieve(self, request, pk=None):
        try:
            quiz = Quiz.objects.get(pk=pk, user=self.request.user)
            serializer = self.get_serializer(quiz, many=False)            
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Quiz.DoesNotExist:
            raise Http404("Quiz not found for self user!")


class RankingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsPlayerPermission]
    serializer_class = RankingSerializer
    queryset = User.objects.filter(quiz__is_finished=True)

    def get_queryset(self):
        category = self.request.query_params.get("category", None)
        filters = {}
        if category:
            filters.update({
                "quiz__category_id": category
            })
        
        sub_accepteds = Answer.objects.filter(
            option__is_correct=True,
            quiz__user=OuterRef("pk")
        ).filter(
            **filters
        ).values("quiz__user_id").annotate(count=Count("*"))

        sub_faults = Answer.objects.filter(
            option__is_correct=False,
            quiz__user=OuterRef("pk")
        ).filter(
            **filters
        ).values("quiz__user_id").annotate(count=Count("*"))
        
        ranking = User.objects.filter(
            **filters            
        ).filter(
            Exists(Quiz.objects.filter(user=OuterRef("pk"), is_finished=True))
        ).values("id", "first_name").annotate(
            accepteds=Coalesce(Subquery(sub_accepteds.values("count")), Value(0)),
            faults=Coalesce(Subquery(sub_faults.values("count")), Value(0)),
        ).annotate(
            points=F("accepteds")-F("faults"),
            name=F("first_name")
        ).annotate(
            total_points=Case(
                When(points__lt=0, then=Value(0)),
                default=F('points')
            )            
        ).values("name", "total_points").order_by("-total_points")        
        return ranking
        
    