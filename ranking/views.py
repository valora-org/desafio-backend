from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from categoria.models import Categoria


@api_view(['GET'])
def rankingGlobal(request):
    rankingGlobal = User.objects.values('username').annotate(total_geral=Sum('jogo__nota')).order_by('-total_geral')
    return Response({"Ranking Global": rankingGlobal},status=status.HTTP_200_OK)

@api_view(['GET'])
def rankingCategoria(request):
    rankingCategoria = Categoria.objects.values('nome').annotate(total_soma=Sum('jogo__nota')).order_by('-total_soma')
    return Response({"Ranking Categoria": rankingCategoria}, status=status.HTTP_200_OK)
