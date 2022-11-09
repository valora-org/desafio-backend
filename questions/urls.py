from django.urls import path
from . import views

urlpatterns = [
    path("questions/", views.QuestionView.as_view()),
    path("questions/<int:question_id>/", views.QuestionSoloView.as_view()),
]
