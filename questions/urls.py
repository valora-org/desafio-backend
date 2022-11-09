from django.urls import path

from questions import views

urlpatterns = [
    path('', views.QuestionView.as_view(), name='list-create-question'),
    path(
        '<str:id>/',
        views.QuestionDetailView.as_view(),
        name='question-detail',
    ),
]
