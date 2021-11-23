from django.contrib.auth.models import User
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import viewsets, status


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = User(**data)
        serializer = UserSerializer(data=user.__dict__)
        try:
            if serializer.is_valid(raise_exception=True):
                result = User.objects.create_user(**serializer.data)
                serializer = UserSerializer(result)
                return Response(serializer.data)
        except Exception as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)