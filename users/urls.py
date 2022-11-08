from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:user_id>/", views.UserSoloView.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("ranking/", views.RankingView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("users/", views.UserView.as_view()),
]
