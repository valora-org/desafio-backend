from rest_framework import viewsets
from rest_framework import permissions

from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
