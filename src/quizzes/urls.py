from django.urls import path
from quizzes import views

urlpatterns = [
    path('play_quiz', views.PlayQuiz.as_view(), name="quizzes"),
    path('get_quiz', views.GetQuiz.as_view(), name="quizzes"),
    path('create_question', views.CreateQuestion.as_view(), name="quizzes"),
    path('create_category', views.CreateCategory.as_view(), name="quizzes")
    
] 