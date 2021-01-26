from django.conf import settings

from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from quiz.categories.views import CategoryViewSet
from quiz.match.views import MatchViewSet
from quiz.questions.views import QuestionViewSet
from quiz.ranking.views import RankingViewSet
from quiz.users.views import AuthViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('auth', AuthViewSet, basename='auth')
router.register('categories', CategoryViewSet, basename='categories')
router.register('match', MatchViewSet, basename='match')
router.register('questions', QuestionViewSet, basename='questions')
router.register('ranking', RankingViewSet, basename='ranking')

app_name = 'api-v1'
urlpatterns = router.urls
