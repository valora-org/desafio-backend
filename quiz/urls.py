from . import views
from django.urls import path, re_path
from rest_framework import routers
from django.conf.urls import include
from .api.viewsets import QuizViewSet

app_name = 'quiz'

router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.quiz, name="Profile"),
]