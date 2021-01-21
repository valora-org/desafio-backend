from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include('config.api_router')),
]
