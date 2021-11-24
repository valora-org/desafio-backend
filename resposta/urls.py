from rest_framework import routers
from . import views
router = routers.SimpleRouter()
router.register(r'resposta', views.RespostaViewSet, basename='resposta')
urlpatterns = router.urls