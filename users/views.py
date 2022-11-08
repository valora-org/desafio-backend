from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import Http404
from .models import User


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, _):

        users = User.objects.all()

        users_serialized = UserSerializer(users, many=True)

        return Response(users_serialized.data, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request: Request):

        user_serialized = UserSerializer(data=request.data)

        try:
            user_serialized.is_valid(raise_exception=True)
            user_serialized.save()

            return Response(user_serialized.data, status=status.HTTP_201_CREATED)

        except ValueError as err:
            return Response(*err.args)

        except IntegrityError as err:
            return Response(
                {"message": "'username' and 'email' must be unique"},
                status=status.HTTP_409_CONFLICT,
            )


class UserSoloView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, _, user_id: int):

        try:
            user = get_object_or_404(User, pk=user_id)
            user_serialized = UserSerializer(user)

            return Response(user_serialized.data, status=status.HTTP_200_OK)

        except Http404:
            return Response(
                {"message": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )


class LoginView(APIView):
    def post(self, request: Request):
        login_serialized = LoginSerializer(data=request.data)
        login_serialized.is_valid(raise_exception=True)

        # Makes sure the data is valid
        user = authenticate(
            email=login_serialized.validated_data["email"].lower(),
            password=login_serialized.validated_data["password"],
        )

        # return user token | error for invalid email or invalid password
        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"message": "Invalid email or password"}, status=status.HTTP_404_NOT_FOUND
        )


class RankingView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, _):
        ranking = User.objects.all().order_by("-points")
        ranking_serialized = UserSerializer(ranking, many=True)

        return Response({"ranking": ranking_serialized.data}, status=status.HTTP_200_OK)
