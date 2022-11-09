from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status

from accounts.models import Account
from accounts.serializers import (
    AccountSerializer,
    AccountUpdateSerializer,
    DetailedAccountSerializer,
    LessDetailedAccountSerializer,
    SignInSerializer,
)
from core.permissions import IsAdminAccount, IsAdminOrReadOnlyAccount
from utils.mixins import SerializerByMethodMixin


class AccountView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnlyAccount]

    serializer_map = {
        'GET': LessDetailedAccountSerializer,
        'POST': AccountSerializer,
    }
    queryset = Account.objects.all()


class AccountDetailView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminAccount]

    queryset = Account.objects.all()

    serializer_map = {
        'GET': DetailedAccountSerializer,
        'PATCH': AccountUpdateSerializer,
        'PUT': AccountUpdateSerializer,
    }

    lookup_field = 'id'


class SignInView(APIView):
    def post(self, request: Request) -> Response:
        serializer = SignInSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response(
                {'detail': 'invalid credentials'}, status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})
