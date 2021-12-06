from django.contrib.auth import get_user_model

from rest_framework import serializers

from users.models import User


# USer Serialiazer used in User Views.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "is_admin", "created_at", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
