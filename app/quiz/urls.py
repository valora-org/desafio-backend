from django.urls import path, re_path
from quiz.views import PlayerQuizList, QuizList, SubmitQuiz, GetQuiz, RankingList, CategoryRankingList

# URLs to access as quiz endpoints
urlpatterns = [
	path("player-quizzes/", PlayerQuizList.as_view()),
	path("quizzes/", QuizList.as_view()),
	path("ranking/", RankingList.as_view()),
	path("ranking/category/", CategoryRankingList.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/$", GetQuiz.as_view()),
	re_path(r"quizzes/submit/(?P<slug>[\w\-]+)/$", SubmitQuiz.as_view()),
]