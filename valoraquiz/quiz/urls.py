from django.urls import include, path
from rest_framework import routers

from quiz import views

app_name = "quiz"


router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"questions", views.QuestionViewSet, basename="questions")
router.register(r"answers", views.AnswerViewSet, basename="answers")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_auth.urls")),
    path("quizzes/", views.QuizViewSet.as_view()),
    path("quizzes/<int:quiz_id>/", views.QuizViewSet.as_view()),
    path("ranking/", views.RankingViewSet.as_view()),
    path("ranking/<int:category_id>/", views.RankingViewSet.as_view()),
]
