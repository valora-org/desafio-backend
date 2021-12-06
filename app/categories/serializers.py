from rest_framework import serializers

from categories.models import Category


# Serializer used in Category Views
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "id")
