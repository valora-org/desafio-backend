from django.urls import path
from django.contrib.auth import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
