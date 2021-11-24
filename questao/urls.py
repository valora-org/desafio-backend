from rest_framework import routers
from . import views
router = routers.SimpleRouter()
router.register(r'questao', views.QuestaoViewSet, basename='questao')
urlpatterns = router.urls