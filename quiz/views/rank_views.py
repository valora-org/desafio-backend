# from user_auth.serializers.profiles_ser import * 
import json
from user_auth.permissions import *
from quiz.models.quiz import *
from desafio_config.utils.views import MixedPermissionModelViewSet
from rest_framework.permissions import *
from rest_framework.decorators import action
from django.http import JsonResponse
from quiz.serializers import *
from quiz.models.rank import * 
from rest_framework import viewsets
from desafio_config.utils.auth import PlayerAuth
from quiz.serializers.uitls import get_rank

class RankViewset(viewsets.ViewSet):
    permission_classes =[IsPlayer]
    authentication_classes = [PlayerAuth]

    def list(self,request):
        player = request.user
        query_params = request.query_params
        player_rank,created = PlayerRank.objects.get_or_create(player=player)
        
        rank = get_rank(player_rank)

        return JsonResponse(
            {'rank_position':rank},safe=False
        )
        
