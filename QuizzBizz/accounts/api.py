from accounts.models import User
from accounts.serializers import LoginSerializer, RegisterSerializer, UserSerializer
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response


class LoginAPI(generics.GenericAPIView):

	#View for login of the user.

	# Respective serializer
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):

		#POST method

		# Validation of login
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data

		# Return response with user and token
		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})


class RegisterAPI(generics.GenericAPIView):

	#View for register a new user.


	# Respective serializer
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):

		#POST method

		# Register a new user 
		print(request.data)
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()


		# Return response with user and token
		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})


class UserAPI(generics.RetrieveAPIView):

	#View for user.

	#Authentication 
	permission_classes = [
		permissions.IsAuthenticated
	]
	# Respective serializer
	serializer_class = UserSerializer
	
	def get_object(self):
		self.request.user