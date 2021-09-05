from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('quiz.core.urls')),
    path('admin/', admin.site.urls),
]
