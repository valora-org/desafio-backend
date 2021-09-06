from django.urls import path

from users import views as v

urlpatterns = [
    path("", v.get_users, name="users"),
    path(
        "login/",
        v.MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("register/", v.register_user, name="register"),
    path("profile/", v.get_user_profile, name="users-profile"),
    path("update/<str:pk>/", v.update_user, name="users-update"),
    path("delete/<str:pk>/", v.delete_user, name="users-delete"),
]
