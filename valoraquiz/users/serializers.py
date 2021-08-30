from django.contrib.auth.models import Group
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "id",
            "username",
        ]
