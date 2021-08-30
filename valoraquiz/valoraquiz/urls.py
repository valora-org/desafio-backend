from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers

import users.urls


router = routers.DefaultRouter()
router.urls.extend(users.urls.urlpatterns)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((router.urls, "valoraquiz"), namespace="api")),
]
