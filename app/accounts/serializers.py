from accounts.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
	"""
		Serializer to login of the User.

	"""
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		"""
			User token validation.

		"""
		user = authenticate(**data)
		if user:
			return user
		raise serializers.ValidationError('Incorrect Credentials')


class CreateSerializer(serializers.ModelSerializer):
	"""
		Serializer to create new User.

	"""
	class Meta:
		model = User
		fields = ('id', 'username', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		"""
			Create User.

		"""
		user = User.objects.create_user(
			username=validated_data["username"],
			password=validated_data["password"]
		)
		return user

class UserSerializer(serializers.ModelSerializer):
	"""
		Serializer to return id and username of the user.

	"""
	class Meta:
		model = User
		fields = ('id', 'username')
