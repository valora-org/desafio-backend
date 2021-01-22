from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import LoginSerializer
from .serializers import SignupSerializer


class AuthViewSet(GenericViewSet):
    """Authentication viewset."""

    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=SignupSerializer)
    @action(methods=['post'], detail=False, url_path='signup')
    def signup(self, request, *args, **kwargs):
        """Create a new user."""
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=LoginSerializer,
                         responses={status.HTTP_200_OK: 'JWT credentials'})
    @action(methods=('post',), detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        """User login."""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
