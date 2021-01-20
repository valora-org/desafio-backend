from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path('users/', include('quiz.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path('api/', include('config.api_router')),
    # DRF auth token
    path('auth-token/', obtain_auth_token),
]
