from django.urls import path, include
from quiz.core import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'choosequiz', views.ChooseQuizViewSet, basename='choosequiz')
router.register(r'startquiz', views.StartQuizViewSet, basename='startquiz')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('result/', views.resultList, name="result-list")
]
