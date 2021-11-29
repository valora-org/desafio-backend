from django.urls import include, path
from rest_framework import routers
from user_auth.views import *
from quiz.views import *
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from desafio_config import settings
from user_auth.router import urls as urls_player
from quiz.router import urls as urls_quiz 

# router.register('quiz',QuizViewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('profiles/',include(urls_player)),
    path('game/',include(urls_quiz)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
