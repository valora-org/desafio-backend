"""
URL configuration for backendchallenge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from accounts.views import UserViewSet
from quiz.views import QuizView
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'quizzes', QuizView, basename='quiz')



urlpatterns = [
    #path("api/", include('quiz.urls', namespace='quiz')),
    path("accounts/", include('accounts.urls', namespace='accounts',)),
    path("api/", include(router.urls)),
    path('api-auth/',  include('rest_framework.urls', namespace='rest_framework',)),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]
