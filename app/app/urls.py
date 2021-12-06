from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api/", include("categories.urls")),
    re_path(r"^api/", include("quizzes.urls")),
    re_path(r"^api/", include("users.urls")),
    re_path(r"^login/", include('rest_framework.urls')),
    re_path(r"^api/token/", TokenObtainPairView.as_view(),
            name='token_obtain_pair'),
    re_path(r"^api/token/refresh/",
            TokenRefreshView.as_view(), name='token_refresh'),
]
