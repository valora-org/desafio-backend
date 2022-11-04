from django.urls import path

from .views import QuizView, RandomQuizQuestionsView

app_name = 'quiz'

urlpatterns = [
    path('', QuizView.as_view(), name='list_quizzes'),
    path(
        'random/<str:quiz_id>/',
        RandomQuizQuestionsView.as_view(),
        name='',
    ),
]
