from django.urls import path
from rest_framework import routers
from . import viewsets

app_name = "api"

router = routers.SimpleRouter()
router.register(r'quiz', viewsets.QuizViewSet, basename="quiz")
router.register(r'category', viewsets.CategoryViewSet, basename="category")
router.register(r'question', viewsets.QuestionViewSet, basename="question")
router.register(r'ranking', viewsets.RankingViewSet, basename="ranking")

urlpatterns = [

]

urlpatterns += router.urls
