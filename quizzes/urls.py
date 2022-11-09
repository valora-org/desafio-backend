from django.urls import path
from . import views

urlpatterns = [
    path("quizzes/", views.QuizView.as_view()),
    path("quizzes/<int:quiz_id>/", views.QuizSoloView.as_view()),
]
