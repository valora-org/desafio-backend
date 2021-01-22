from django.conf import settings

from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from quiz.categories.views import CategoryViewSet
from quiz.users.views import AuthViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('auth', AuthViewSet, basename='auth')
router.register('categories', CategoryViewSet, basename='categories')

app_name = 'api-v1'
urlpatterns = router.urls
