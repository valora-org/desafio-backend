from rest_framework import serializers
from .models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate
from .models import Point


class PointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = '__all__'


class PlayerSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
        )
        read_only_fields = [
            'id',
            'username'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists'})
        return super().validate(attrs)

    def create(self, validated_data):
        random_code = get_random_string(5)

        validated_data['username'] = f'player_{random_code}'
        return User.objects.create_user(**validated_data)


class AdminSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'is_superuser',
            'is_staff',
        )
        read_only_fields = [
            'id',
            'is_superuser',
            'is_staff',
            'username'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists'})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['is_superuser'] = True
        validated_data['is_staff'] = True

        random_code = get_random_string(7)
        validated_data['username'] = f'admin_{random_code}'
        return User.objects.create_user(**validated_data)


class UserAuthenticateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'is_superuser',
        )


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
        )

    def validate(self, attrs):
        user_token = self.context['request'].user
        current_user = self.instance
        if not user_token.is_superuser:
            if user_token.id == current_user.id:
                pass
            else:
                raise serializers.ValidationError(
                    {'validation': 'You are not allowed to update this instance.'})
        return super().validate(attrs)


class ResetUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=65, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'old_password',
            'password'
        )

        read_only_fields = [
            'id',
            'email',
        ]

    def validate(self, attrs):
        username = self.instance.username
        old_password = attrs.get('old_password', '')
        password = attrs.get('password', '')
        if old_password == password:
            raise serializers.ValidationError(
                {'password': 'Set a diferent password'})
        user_authenticate = authenticate(username=username, password=old_password)

        if not user_authenticate:
            user = User.objects.filter(username=username, password=old_password)
        else:
            user = user_authenticate

        if not user:
            raise serializers.ValidationError(
                {'password': 'Wrong old password'})
        return super().validate(attrs)


class UserRankingSerializer(serializers.ModelSerializer):
    global_points = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'global_points'
        )


class UserCategoryRankingSerializer(serializers.ModelSerializer):
    category_points = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'category_points',
        )
