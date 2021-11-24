from rest_framework import serializers

from questao.models import Questao


class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = '__all__'
