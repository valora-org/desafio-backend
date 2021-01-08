from django.contrib import admin
from django.urls import path
from apps.quiz.views import match

urlpatterns = [
    path('admin/', admin.site.urls),
    path('match/', match)
]
