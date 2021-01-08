from django.contrib import admin
from django.urls import path, include
from apps.quiz.views import MatchViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('matchs', MatchViewSet, basename='Matchs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
