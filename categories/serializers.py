from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        name = validated_data.pop("name").title()

        category = Category.objects.create(name=name, **validated_data)

        return category

    def update(self, instance: Category, validated_data):
        for key, item in validated_data.items():
            setattr(instance, key, item)

        instance.save()

        return instance
