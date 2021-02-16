"""quiz URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken import views as token_views
from rest_framework import routers
from quiz.views import (QuestionViewSet, QuizViewSet, CategoryViewSet,
                        GameViewSet)


router = routers.SimpleRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'quizes', QuizViewSet)
router.register(r'game', GameViewSet, basename='game')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', token_views.obtain_auth_token),
] + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

urlpatterns += router.urls
