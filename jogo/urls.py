from django.urls import path
from . import views

urlpatterns = [
    path('iniciar-jogo/', views.JogoAPIView.as_view()),
    path('finalizar-jogo/<int:id>', views.JogoAPIView.as_view()),
    path('buscar-jogo/<int:id>', views.JogoAPIView.as_view()),
]