from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from quiz.core.permissions import IsPlayer, default_permissions

from .models import CategoryScore, Profile
from .serializers import CategoryScoreSerializer, ProfileSerializer


class RankingViewSet(ReadOnlyModelViewSet):
    """Ranking of players.

    retrieve:
    Get general ranking.

    list:
    Get ranking of a given category.
    """

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [*default_permissions, IsPlayer]
    lookup_field = 'category_id'

    def retrieve(self, request, *args, **kwargs):
        """Get ranking of a given category."""
        category_id = kwargs['category_id']
        instances = get_list_or_404(CategoryScore, category__id=category_id)
        sorted_instances = sorted(instances,
                                  key=self.sort_category_score_key,
                                  reverse=True)
        serializer = CategoryScoreSerializer(sorted_instances, many=True)
        return Response(serializer.data)

    def sort_category_score_key(self, category_score):
        """Get key for sorting category score."""
        return category_score.score

    def filter_queryset_key(self, profile):
        """Get key for sorting profile key."""
        return profile.general_score

    def filter_queryset(self, queryset):
        """Sort general queryset."""
        return sorted(queryset, key=self.filter_queryset_key, reverse=True)
