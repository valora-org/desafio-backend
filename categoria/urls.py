from rest_framework import routers
from . import views
router = routers.SimpleRouter()
router.register(r'categorias', views.CategoriaViewSet, basename='categorias')
urlpatterns = router.urls
