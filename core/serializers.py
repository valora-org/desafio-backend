from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Usuario, Pergunta, Resposta, Categoria, Quiz


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ['pergunta_texto']

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    perguntas = PerguntaSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'

