from rest_framework import serializers

from jogo.models import Jogo
from questao.models import Questao
from questao.serializers import QuestaoSerializer


class JogoSerializer(serializers.ModelSerializer):
    questoes = QuestaoSerializer(many=True)
    class Meta:
        model = Jogo
        fields = ('id','usuario','categoria','nota','questoes')
