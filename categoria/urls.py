from rest_framework import routers
from . import views
router = routers.SimpleRouter()
router.register(r'categoria', views.CategoriaViewSet, basename='categoria')
urlpatterns = router.urls
