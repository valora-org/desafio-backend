from django.urls import path

from quizzes import views

urlpatterns = [
    path('', views.QuizView.as_view(), name='list-create-quiz'),
    path('<str:id>/', views.QuizDetailView.as_view(), name='quiz-detail'),
    path(
        'random/<str:id>/',
        views.RandomQuestionsQuizView.as_view(),
        name='random-questions-quiz',
    ),
    path(
        'questions/<str:id>/',
        views.QuizQuestion.as_view(),
        name='quiz-questions',
    ),
]
