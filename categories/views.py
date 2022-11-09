from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from categories.models import Category
from categories.serializers import (
    CategorySerializer,
    DetailedCategorySerializer,
)
from core.permissions import IsAdminOrReadOnly
from utils.mixins import SerializerByMethodMixin


class CategoryView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Category.objects.all()

    serializer_map = {
        'GET': DetailedCategorySerializer,
        'PATCH': CategorySerializer,
        'PUT': CategorySerializer,
    }

    lookup_field = 'id'
