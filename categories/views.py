from rest_framework import generics

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    lookup_url_kwarg = 'category_id'
