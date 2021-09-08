from django.urls import path, re_path
from rest_framework import routers
from django.conf.urls import include
from quiz.api import viewsets
from rest_framework.authtoken import views

app_name = 'quiz'

router = routers.DefaultRouter()
router.register(r'quiz', viewsets.QuizViewSet, basename='Quiz')
router.register(r'question', viewsets.QuestionViewSet)
router.register(r'answer', viewsets.AnswerViewSet)
router.register(r'user', viewsets.UserViewSet)
router.register(r'ranking', viewsets.RankingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]