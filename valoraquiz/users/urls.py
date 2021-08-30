from django.urls import include, path
from rest_framework import routers

from users import views

app_name = "users"


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_auth.urls")),
]
