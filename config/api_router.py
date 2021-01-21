from django.conf import settings

from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from quiz.users.views import AuthViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('auth', AuthViewSet, basename='auth')

app_name = 'api-v1'
urlpatterns = router.urls
