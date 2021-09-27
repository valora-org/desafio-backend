from django.urls import path
from django.urls import include
from rest_framework import routers



from . import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'perguntas', views.PerguntaViewSet)
router.register(r'respostas', views.RespostaViewSet)
router.register(r'quizs', views.QuizViewSet)
router.register(r'categorias', views.CategoriaViewSet)

urlpatterns = [
    # path('core/', include(router.urls)),
    path('', views.index, name='index'),
    path('perguntas/', views.crear_perguntas, name='perguntas'),
    path('play/', views.play, name='play'),
    path('resposta/', views.resposta, name='resposta'),
    path('ranking/', views.ranking, name='ranking')
]