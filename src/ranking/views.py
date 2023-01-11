from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from accounts.models import User
from ranking.models import Ranking
from ranking.serializers import UserRankingSerializer, RankingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class GlobalRanking(PermissionRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    permission_required = ['accounts.can_consult_ranking']
    def get(self, request):
        all_users = UserRankingSerializer(data=User.get_global_ranking(), many=True)
        all_users.is_valid()
        return Response(all_users.data)

class CategoryRanking(PermissionRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]
    permission_required = ['accounts.can_consult_ranking']
    def post(self, request):
        category = request.data.get("category")
        if not category:
            return Response({"Permissão negada":"Parâmetro 'category' não foi passado"})
        all_users = RankingSerializer(data=Ranking.objects.filter(category=category).order_by('-points'), many=True)
        all_users.is_valid()
        return Response(all_users.data)


# Create your views here.
