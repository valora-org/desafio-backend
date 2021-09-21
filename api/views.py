from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            user = User.objects.create_user(data['username'],
                                            data['email'],
                                            data['password'])

            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response({'mensage': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


