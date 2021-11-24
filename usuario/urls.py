from rest_framework import routers
from . import views
router = routers.SimpleRouter()
router.register(r'usuario', views.UsuarioViewSet, basename='usuario')
urlpatterns = router.urls
