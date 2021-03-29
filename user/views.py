from rest_framework.generics import (ListAPIView,
                                     GenericAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
from .serializers import (PlayerSignupSerializer,
                          AdminSignupSerializer,
                          UserAuthenticateSerializer,
                          UserListSerializer,
                          UserRetrieveSerializer,
                          UserUpdateSerializer,
                          ResetUserPasswordSerializer,
                          UserRankingSerializer,
                          UserCategoryRankingSerializer)
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import serializers
from .models import User
import jwt


class RegisterPlayerView(GenericAPIView):
    serializer_class = PlayerSignupSerializer

    def post(self, request):
        serializer = PlayerSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAdminView(GenericAPIView):
    serializer_class = AdminSignupSerializer

    def post(self, request):
        serializer = AdminSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthenticateUserView(GenericAPIView):
    serializer_class = UserAuthenticateSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        try:
            object_pass = User.objects.get(email=email)
        except:
            return Response({'detail': 'Invalid credentials'})

        username = object_pass.username
        user = authenticate(username=username, password=password)

        if not user:
            user = User.objects.filter(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': username}, str(settings.JWT_SECRET_KEY))

            data = {'email': email, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ListUserProfileView(ListAPIView):

    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.all()


class RetrieveUserProfileView(RetrieveAPIView):

    serializer_class = UserRetrieveSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        user_token = self.request.parser_context['request'].user
        if not user_token.is_superuser:
            if user_token.id == self.kwargs['id']:
                pass
            else:
                raise serializers.ValidationError(
                    {'validation': 'You are not allowed to search this profile.'})
        return User.objects.filter(id=self.kwargs['id'])


class DeleteUserProfileView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        queryset = User.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_destroy(self, instance):
        user_token = self.request.parser_context['request'].user
        if not user_token.is_superuser:
            if user_token == instance:
                pass
            else:
                raise serializers.ValidationError(
                    {'validation': 'You are not allowed to delete another user profile.'})
        instance.delete()


class UpdateUserProfile(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = User.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()


class ChangePassUserView(UpdateAPIView):
    serializer_class = ResetUserPasswordSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = User.objects.filter(id=self.kwargs['id'])
        return queryset

    def perform_update(self, serializer):
        serializer.save()


class GlobalRankingView(ListAPIView):

    serializer_class = UserRankingSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        list_users = []
        queryset = User.objects.all()
        for row in queryset:
            if not row.points.values():
                global_points = 0
            else:
                point_values = row.points.values()
                for row2 in point_values:
                    global_points = row2["global_point"]

            user_object = {
                "id": row.id,
                "email": row.email,
                "global_points": str(global_points)
            }
            list_users.append(user_object)

        def get_my_key(obj):
            return obj['global_points']
        list_users.sort(key=get_my_key, reverse=True)
        serializer = self.get_serializer(list_users, many=True)
        return Response(serializer.data)


class CategoryRankingView(RetrieveAPIView):

    serializer_class = UserCategoryRankingSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "category"

    def retrieve(self, request, *args, **kwargs):
        list_users = []
        category = self.kwargs['category']

        queryset = User.objects.all()
        for row in queryset:
            if not row.points.values():
                points = 0
            else:
                point_values = row.points.values()
                for row2 in point_values:
                    if row2["category"] == category:
                        points = row2["points"]

            user_object = {
                "id": row.id,
                "email": row.email,
                "category": category,
                "category_points": str(points)
            }
            list_users.append(user_object)

            def get_my_key(obj):
                return obj['category_points']
            list_users.sort(key=get_my_key, reverse=True)

        return Response(list_users)
