from rest_framework import serializers

from questao.models import Questao
from resposta.models import Resposta
from resposta.serializers import RespostaSerializer



class QuestaoSerializer(serializers.ModelSerializer):
    respostas = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Questao
        fields = ('id','texto','categoria','respostas')
