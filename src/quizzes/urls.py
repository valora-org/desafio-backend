from django.urls import path
from quizzes.views import PlayQuizz

urlpatterns = [
    path('play_quizz', PlayQuizz.as_view(), name="quizzes")
] 