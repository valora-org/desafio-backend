from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# URLs to access API endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('accounts/', include('accounts.urls')),
    path('nested_admin', include('nested_admin.urls')),
]
