from django.urls import path

from answers import views

app_name = 'answer'

urlpatterns = [
    path(
        '',
        views.AnswerView.as_view(),
        name='list-create-answer',
    ),
    path(
        '<str:answer_id>/',
        views.AnswerDetailView.as_view(),
        name='answer-detail',
    ),
]
