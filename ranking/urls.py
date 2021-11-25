from django.urls import path
from . import views

urlpatterns = [
    path('global/', views.rankingGlobal),
    path('categoria/', views.rankingCategoria),
]