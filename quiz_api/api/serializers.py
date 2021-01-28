from rest_framework import serializers
from quiz_api.models import Pergunta, Classificacao

class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','nome_classificacao')
        model = Classificacao
        



class PerguntaSerializer(serializers.ModelSerializer):
    #nome_classificacao = ClassificacaoSerializer()
    classificacao_completa = serializers.SerializerMethodField()
    class Meta:
        fields = ('id', 'classificacao', 'classificacao_completa','pergunta', 'resposta','opcao1', 'opcao2', 'opcao3')
        model = Pergunta
    
    def get_classificacao_completa(self, obj):
        return "%s" % (obj.classificacao)