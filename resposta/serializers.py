from rest_framework import serializers

from questao.models import Questao
from resposta.models import Resposta
from resposta.validators import max_resposta


class RespostaSerializer(serializers.ModelSerializer):
    texto = serializers.CharField(required=True, max_length=255)
    questao = serializers.PrimaryKeyRelatedField(required=True,queryset=Questao.objects.all()
                                                 ,validators=[max_resposta])
    correta = serializers.BooleanField(required=True)
    class Meta:
        model = Resposta
        fields = '__all__'

