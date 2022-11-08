from django.urls import path

from quizzes import views

urlpatterns = [
    path('', views.QuizView.as_view(), name='list-create-quiz'),
    path('<str:quiz_id>/', views.QuizDetailView.as_view(), name='quiz-detail'),
    path(
        'random/<str:quiz_id>/',
        views.RandomQuestionsQuizView.as_view(),
        name='random-questions-quiz',
    ),
]
