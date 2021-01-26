from rest_framework import serializers

from .models import CategoryScore, Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for profile."""

    class Meta:
        """Meta info for category serializer."""

        model = Profile
        fields = ['username', 'name', 'general_score']
        ordering = ['-general_score', 'username']


class CategoryScoreSerializer(serializers.ModelSerializer):
    """Serializer for profile."""

    username = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    def get_username(self, obj):
        """Get username."""
        return obj.profile.player.username

    def get_name(self, obj):
        """Get name."""
        return obj.profile.player.name

    class Meta:
        """Meta info for category serializer."""

        model = CategoryScore
        fields = ['score', 'username', 'name']
        ordering = ['-score', 'username']
