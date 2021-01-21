from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    """Serializer for signup user."""

    password = serializers.CharField(max_length=150,
                                     min_length=6,
                                     write_only=True)

    def create(self, validated_data):
        """Create a new user."""
        return User.objects.create_user(**validated_data)

    class Meta:
        """Meta information for signup serializer."""

        model = User
        fields = ['username', 'name', 'role', 'password']
        extra_kwargs = {
            'username': {
                'required': True
            },
            'role': {
                'required': True
            },
            'password': {
                'required': True
            }
        }
        ref_name = 'Sign up credentials'


class LoginSerializer(serializers.Serializer):
    """Serializer for login user."""

    password = serializers.CharField(max_length=150,
                                     min_length=6,
                                     write_only=True)
    username = serializers.CharField(max_length=150,
                                     min_length=6,
                                     write_only=True)

    def validate(self, attrs):
        """Validate credentials and get user tokens."""
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed(_('Invalid credentials'))
        refresh = RefreshToken.for_user(user)
        return {'access': str(refresh.access_token), 'refresh': str(refresh)}

    class Meta:
        """Meta information for login serializer."""

        ref_name = 'Login credentials'
