from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from api.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='User')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
