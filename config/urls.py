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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views as token_views
from rest_framework import routers
from quiz.views import (QuestionViewSet, QuizViewSet, CategoryViewSet,
                        GameViewSet, RankingViewSet, AnswerViewSet)


router = routers.SimpleRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'quizes', QuizViewSet)
router.register(r'game', GameViewSet, basename='game')
router.register(r'ranking', RankingViewSet, basename='ranking')


schema_view = get_schema_view(
   openapi.Info(
      title="Quiz API",
      default_version='v1',
      description="Api para gerar e promover questionários.",
      contact=openapi.Contact(email="diogooo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', token_views.obtain_auth_token),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc')
] + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

urlpatterns += router.urls
