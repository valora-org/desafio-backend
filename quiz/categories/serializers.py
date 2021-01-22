from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for caregory."""

    class Meta:
        """Meta info for category serializer."""

        model = Category
        fields = ['id', 'name', 'questions_count']
        read_only_fields = ['questions_count']
