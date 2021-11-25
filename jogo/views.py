from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Count,Sum
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from categoria.models import Categoria
from jogo.models import Jogo
from jogo.serializers import JogoSerializer
from questao.models import Questao
from resposta.models import Resposta
import json

class JogoAPIView(APIView):

    def post(self, request):
        usuario = request.user
        categoria = get_object_or_404(Categoria, id=request.data['categoria'])
        questoes = Questao.objects.annotate(qtd_respostas=Count('respostas')).filter(qtd_respostas=3).filter(
            categoria=categoria).order_by('?').values_list('id',flat=True)[:10]
        if questoes.count() < 10:
            return Response({'error': 'Categoria não possui questões válidas suficientes'},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            jogo = Jogo.objects.create(usuario=usuario,categoria=categoria)
            jogo.questoes.set(questoes)
            return Response({"status": "successo", "data": JogoSerializer(jogo).data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "data": e}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        item = get_object_or_404(Jogo,id=id)
        serializer = JogoSerializer(item)
        return Response({"status": "success", "data": serializer.data},
                        status=status.HTTP_200_OK)

    def put(self, request,id=None):
        jogo = get_object_or_404(Jogo, id=id)

        if jogo.nota is not None or jogo.usuario!=request.user:
            return Response({'status': 'error','data':'Jogo indisponivel'},
                            status=status.HTTP_400_BAD_REQUEST)

        respostas = Resposta.objects.filter(questao__in=jogo.questoes.values_list('id',flat=True))
        nota=0
        for resposta in request.data['respostas']:
            acertou = respostas.filter(questao=resposta['questao']).filter(id=resposta['resposta']).\
                values_list('correta',flat=True).get()
            if acertou:
                nota +=1
        jogo.nota = nota
        jogo.save()

        rankingGlobal = User.objects.values('username').annotate(total_geral=Sum('jogo__nota')).order_by('-total_geral')
        return Response({"Nota do quiz Atual": jogo.nota, "Ranking Global": rankingGlobal})