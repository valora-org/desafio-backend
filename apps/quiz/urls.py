from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MatchesGameFilterCategoryAPIView, CategoryViewSet, MatchGameViewSet, SelectionViewSet

router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('matchGame', MatchGameViewSet)
router.register('selection', SelectionViewSet)

urlpatterns = [
    path('matchGame/category/<int:category_pk>/',
         MatchesGameFilterCategoryAPIView.as_view(),
         name='matchGameFilter')
]
