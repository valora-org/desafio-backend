from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/questions/", include("questions.urls")),
    path("api/rank/", include("rank.urls")),
]
