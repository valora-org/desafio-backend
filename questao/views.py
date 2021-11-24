from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from questao.models import Questao
from questao.serializers import QuestaoSerializer


class QuestaoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer