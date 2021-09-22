from rest_framework.serializers import ModelSerializer

from api.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'is_active', 'is_admin')

