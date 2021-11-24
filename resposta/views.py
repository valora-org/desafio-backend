from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from resposta.models import Resposta
from resposta.serializers import RespostaSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

    def update(self, request, pk=None):
        response = {'message': 'Função Desabilitada'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Função Desabilitada'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)