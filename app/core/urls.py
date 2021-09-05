from django.urls import path
from rest_framework.routers import SimpleRouter
'''
from .views import (
    CategoryAPIView, QuestionAPIView, AnswerAPIView, CategoryQuestionAPIView,
    CategoriesAPIView, QuestionsAPIView, AnswersAPIView,
    CategoriesQuestionsAPIView
)


urlpatterns = [
    path('category/<str:pk>/', CategoryAPIView.as_view(), name='category'),
    path('category/', CategoriesAPIView.as_view(), name='categories'),
    path('question/<str:pk>/', QuestionAPIView.as_view(), name='question'),
    path('question/', QuestionsAPIView.as_view(), name='questions'),
    path('answer/<str:pk>/', AnswerAPIView.as_view(), name='answer'),
    path('answer/', AnswersAPIView.as_view(), name='answers'),
    path(
        'category-question/',
        CategoryQuestionAPIView.as_view(),
        name='categories-questions'
    ),
    path(
        'category-question/<str:pk>/',
        CategoriesQuestionsAPIView.as_view(),
        name='category-question'
    ),
]
'''
from .views import (
    CategoryViewSet,
    QuestionViewSet,
    AnswerViewSet,
    CategoryQuestionViewSet,
    QuizAPIView,
    RankingViewSet,
    UserViewSet
)

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)
router.register('categories-questions', CategoryQuestionViewSet)
router.register('ranking', RankingViewSet)
router.register('register', UserViewSet)
urlpatterns = [
    path(
        'quiz/category/<str:category_id>/',
        QuizAPIView.as_view(),
        name='quiz'
    ),
]