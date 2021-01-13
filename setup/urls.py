from django.contrib import admin
from django.urls import path, include

from apps.quiz.urls import router


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('apps.quiz.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
