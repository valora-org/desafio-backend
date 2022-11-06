from rest_framework import generics

from categories.models import Category
from categories.serializers import (
    CategorySerializer,
    DetailedCategorySerializer,
)
from utils.mixins import SerializerByMethodMixin


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = Category.objects.all()

    serializer_map = {
        'GET': DetailedCategorySerializer,
        'PATCH': CategorySerializer,
        'PUT': CategorySerializer,
    }

    lookup_url_kwarg = 'category_id'
