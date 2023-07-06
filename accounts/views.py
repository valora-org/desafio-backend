from django.shortcuts import render
from accounts.models import CustomUser as User
from accounts.serializers import UserSerializer
from rest_framework import viewsets, permissions
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]