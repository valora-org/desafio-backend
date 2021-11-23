from rest_framework import routers
from . import views
router = routers.SimpleRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')
urlpatterns = router.urls
