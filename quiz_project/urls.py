from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quiz_api.api.viewsets import PerguntaViewSet, ClassificacaoViewSet

router = routers.DefaultRouter()
router.register('v1/perguntas', PerguntaViewSet)
router.register('v1/classificacao', ClassificacaoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('users.urls')),
    path('', include('quiz_game.urls')),
]