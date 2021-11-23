from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework import viewsets


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
