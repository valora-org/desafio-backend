from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Request, Response, status

from accounts.models import Account
from accounts.serializers import (
    AccountSerializer,
    AccountUpdateSerializer,
    DetailedAccountSerializer,
    LessDetailedAccountSerializer,
    SignInSerializer,
)
from utils.mixins import SerializerByMethodMixin


class AccountView(SerializerByMethodMixin, generics.ListCreateAPIView):
    serializer_map = {
        'GET': LessDetailedAccountSerializer,
        'POST': AccountSerializer,
    }
    queryset = Account.objects.all()


class AccountDetailView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = Account.objects.all()

    serializer_map = {
        'GET': DetailedAccountSerializer,
        'PATCH': AccountUpdateSerializer,
        'PUT': AccountSerializer,
    }

    lookup_url_kwarg = 'account_id'


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
