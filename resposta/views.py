from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from resposta.models import Resposta
from resposta.serializers import RespostaSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    permission_classes = [IsAdminUser]
