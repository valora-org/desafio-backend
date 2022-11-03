from django.urls import path

from .views import AleatoryQuestion, QuizView

app_name = 'quiz'

urlpatterns = [
    path('', QuizView.as_view(), name='quiz'),
    path(
        'aleatory/<str:quiz_id>/',
        AleatoryQuestion.as_view(),
        name='aleatory_question',
    ),
]
