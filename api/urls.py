from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from api.viewsets import UserViewSet, CategoryViewSet, AnswerViewSet, QuestionViewSet, QuizViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'answer', AnswerViewSet, basename='answer')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'quiz', QuizViewSet, basename='quiz')

urlpatterns = [
    path('', include(router.urls))
]