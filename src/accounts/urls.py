from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('api/token', ObtainAuthToken.as_view(), name="token")
] 