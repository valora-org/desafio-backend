from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "points",
            "is_superuser",
            "is_staff",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "points",
            "is_superuser",
            "is_staff",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, email: str):
        email = email.lower()
        return email

    def validate_password(self, password: str):
        password = make_password(password)

        return password

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        return user

    def update(self, instance: User, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
