from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
# from api.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('quiz.urls', 'quiz'))),

    # path('api_generate_token/', views.obtain_auth_token),
    # path('login/', Login.as_view(), name='login'),
    # path('logout/', Logout.as_view())
]
