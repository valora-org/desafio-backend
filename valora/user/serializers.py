from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def save(self):
        if User.objects.filter(email=self.validated_data['email']).count() > 0:
            raise serializers.ValidationError(u'This email address is already registered.')
        conta = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")

    class Meta:
        model = UserProfile
        fields = ('sequential', 'username', 'points')


class TempUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")

    ranking = serializers.SerializerMethodField('get_ranking')

    def get_ranking(self, obj):
        return "http://127.0.0.1:8000/ranking/"

    class Meta:
        model = UserProfile
        fields = ('sequential', 'username', 'total_points', 'temp_points', 'ranking')
