from accounts.models import User
from accounts.serializers import LoginSerializer, CreateSerializer, UserSerializer
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response


class Login(generics.GenericAPIView):
	"""
		View for login of the user.

	"""

	# Respective serializer
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		"""
			POST method

		"""

		# Validation of login
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data

		# Return response with user and token
		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})


class Create(generics.GenericAPIView):
	"""
		View for create new user.

	"""

	# Respective serializer
	serializer_class = CreateSerializer

	def post(self, request, *args, **kwargs):
		"""
			POST method

		"""

		# Create new user 
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()

		# Return response with user and token
		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})



