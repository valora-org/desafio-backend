from django.contrib import admin
from django.urls import path, include
from apps.quiz.views import CategoryViewSet, MatchViewSet, SelectionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='Category')
router.register('match', MatchViewSet, basename='Match')
router.register('selection', SelectionViewSet, basename='Selection')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
