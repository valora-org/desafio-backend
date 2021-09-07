from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from rank.models import Rank


class RankSerializer(serializers.ModelSerializer):
    category = SerializerMethodField()
    profile = SerializerMethodField()

    class Meta:
        model = Rank
        fields = "__all__"

    def get_category(self, obj):
        return obj.category.name

    def get_profile(self, obj):
        return obj.profile.first_name

