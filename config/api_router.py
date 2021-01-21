from django.conf import settings

from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = 'api'
urlpatterns = router.urls
