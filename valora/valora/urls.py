"""valora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from quiz.views import CategoryAdminViewSet, QuestionAdminViewSet, CategoryViewSet
from user.views import RankingAPIView

api_router = routers.DefaultRouter()
api_router.register(r"category", CategoryAdminViewSet)
api_router.register(r"question", QuestionAdminViewSet)
api_router.register(r"category_list", CategoryViewSet, basename='category-list')
api_router.register(r"ranking", RankingAPIView, basename='ranking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('quiz/', include('quiz.urls')),
    path('', include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls')),# Para Teste
    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/',include('rest_auth.registration.urls')),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),# Para Teste


]
