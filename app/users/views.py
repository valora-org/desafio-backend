
from django.contrib.auth import authenticate, login

from rest_framework import status, viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class CreateUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        if "is_admin" in request.data and request.data["is_admin"] == True:
            if request.user.is_superuser:
                serialized_data = self.serializer_class(data=request.data)
                if serialized_data.is_valid(raise_exception=True):
                    serialized_data.save()
                    return Response(data=serialized_data.data, status=201)
            else:
                return Response(data="You don't have permission to perform this action", status=403)
        else:
            data = request.data.copy()
            data["is_admin"] = False
            serialized_data = self.serializer_class(data=data)
            if serialized_data.is_valid(raise_exception=True):
                serialized_data.save()
                return Response(data=serialized_data.data, status=201)
