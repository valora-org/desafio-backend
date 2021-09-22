from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
