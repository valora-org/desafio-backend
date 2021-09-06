from . import views
from django.urls import path, re_path

app_name = 'quiz'

urlpatterns = [
    path('', views.profile, name="Profile"),
]