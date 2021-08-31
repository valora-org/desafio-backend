from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import users.urls
import quiz.urls


router = routers.DefaultRouter()
router.urls.extend(users.urls.urlpatterns)
router.urls.extend(quiz.urls.urlpatterns)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((router.urls, "valoraquiz"), namespace="api")),
]
