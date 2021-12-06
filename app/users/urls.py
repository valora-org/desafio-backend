from django.urls import re_path

from users.views import CreateUserViewSet, CreateSuperUserViewSet

app_name = "users"
urlpatterns = [
    re_path(r"^create-user/$",
            CreateUserViewSet.as_view({"post": "create"}), name="create_user"),
    re_path(r"^create-superuser/$",
            CreateSuperUserViewSet.as_view({"post": "create"}), name="create_superuser"),
    re_path(r"^users/$",
            CreateUserViewSet.as_view({"get": "list"}), name="list_users"),
]
