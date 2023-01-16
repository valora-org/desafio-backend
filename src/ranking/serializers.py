from rest_framework import serializers
from ranking.models import Ranking

class UserRankingSerializer(serializers.Serializer):
    email = serializers.CharField()
    all_rank_points = serializers.CharField()
    
class RankingSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField()
    
    class Meta:
        model = Ranking
        fields = ['player','category','points']
    
    def get_player(self, obj):
        return obj.player.email
