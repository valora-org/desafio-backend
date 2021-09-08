from . import views
from django.urls import path, re_path
from rest_framework import routers
from django.conf.urls import include
from quiz.api import viewsets

app_name = 'quiz'

router = routers.DefaultRouter()
router.register(r'/quiz', viewsets.QuizViewSet)
router.register(r'/question', viewsets.QuestionViewSet)
router.register(r'/answer', viewsets.AnswerViewSet)
router.register(r'/user', viewsets.UserViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    # path('', views.quiz, name="Profile"),
]