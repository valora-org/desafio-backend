from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

from .api_doc import redoc_view
from .api_doc import swagger_view

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # Swagger/redoc
    path('', swagger_view, name='schema-swagger-ui'),
    path('redoc/', redoc_view, name='schema-redoc'),
    #
    path('api/v1/', include('config.api_router')),
]
