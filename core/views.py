from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.models import Usuario, Pergunta, Resposta, Categoria, Quiz
from core.serializers import UserSerializer, GroupSerializer, PerguntaSerializer, UsuarioSerializer, CategoriaSerializer, QuizSerializer, RespostaSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import json

'''
Metodo POST inicial para criar quiz
Necessario informar a categoria
'''
@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def index(request):
    dados = request.data
    try:
        usuario = Usuario.objects.get(user = request.user)
    except:
        return Response({"detail": "Usuário sem permissão"}, status=status.HTTP_400_BAD_REQUEST)
    if usuario.admin: #verifica se eh admin ou player
        return Response({"detail": "Admin, para criar Perguntas use a URL /perguntas"}, status=status.HTTP_404_NOT_FOUND)
    else:
        quiz = Quiz.objects.filter(usuario=usuario) #busca os quizs do player
        em_aberto = False
        for q in quiz: 
            if q.questao_respondida < 10: #verifica se tem algum quiz em aberto(com menos de 10 perguntas respondidas), caso exista, pega o primeiro
                em_aberto = True
                break
        if quiz.exists() and em_aberto: #se existe quiz aberto, informa para o player que outro endpoint
            return Response({"detail": f"Existe um quiz em aberto da categoria {quiz.first().perguntas.first().categoria}",
                                "information": "User a URL /play para responde o Quiz"},
                                status=status.HTTP_302_FOUND)
        else:
            try:
                categoria = Categoria.objects.get(categoria_texto=dados["categoria"])
            except Categoria.DoesNotExist:
                return Response({"detail": "Informe uma categoria válida"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"detail": "Informe uma categoria"}, status=status.HTTP_400_BAD_REQUEST)
            quiz = Quiz.criar(usuario, dados["categoria"])
            return Response(QuizSerializer(quiz).data, status=status.HTTP_201_CREATED) #serializa o quiz e envia para visualizacao


'''
Metodo POST para criar perguntas
Necessario informar a categoria, pergunta, alterarnativa correta, alternativa1, alteranativa2
'''
@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def criar_perguntas(request):
    dados = request.data
    try:
        usuario = Usuario.objects.get(user = request.user)
    except:
        return Response({"detail": "Usuário sem permissão"}, status=status.HTTP_400_BAD_REQUEST)
    if usuario.admin: #verifica se eh admin ou player
        try:
            categoria = Categoria.objects.get(categoria_texto = dados["categoria"]) #verifica se cateogira existe
            pergunta = Pergunta.objects.create(pergunta_texto = dados["pergunta"], categoria = categoria) #cria pergunta para a categoria
            Resposta.objects.create(pergunta = pergunta, resposta_texto = dados["alternativa_correta"], correta = True) #altarnativa correta
            #outras duas alternativas
            Resposta.objects.create(pergunta = pergunta, resposta_texto = dados["alternativa1"])
            Resposta.objects.create(pergunta = pergunta, resposta_texto = dados["alternativa2"])
        except Categoria.DoesNotExist:
            return Response({"detail": "Informe uma categoria válida"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pergunta.delete() #caso ocorra um erro, deletar a pergunta e junto ira as respostas caso tenha sido criada
            return Response({"detail": "Paramentros incorretos"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Sucesso"}, status=status.HTTP_201_CREATED)
    else: #caso o usuario nao eh admin
        return Response({"detail": "Você não é admin"}, status=status.HTTP_400_BAD_REQUEST)

'''
Metodo GET para consultar pergunta
'''
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def play(request):
    try:
        usuario = Usuario.objects.get(user = request.user)
    except:
        return Response({"detail": "Usuário sem permissão"}, status=status.HTTP_400_BAD_REQUEST)
    pergunta, alternativas = Quiz.play(usuario)
    if pergunta is None:
        return Response({"detail": "Inicie o quiz"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"Pergunta": f"{pergunta.pergunta_texto}",
                    "a": f"{alternativas[0]}",
                    "b": f"{alternativas[1]}",
                    "c": f"{alternativas[2]}",})

'''
Metodo POST responder questionario
'''
@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def resposta(request):
    dados = request.data
    try:
        usuario = Usuario.objects.get(user = request.user)
    except:
        return Response({"detail": "Usuário sem permissão"}, status=status.HTTP_400_BAD_REQUEST)
    acertou = Quiz.verificar(usuario, dados["resposta"])
    if acertou is None:
        return Response({"detail": "Alternativa não existe, tente novamente"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({f"Resposta: {'CERTA' if acertou else 'ERRADA'}"})
        
        
'''
Metodo para consultar o ranking
return: ranking
'''
@api_view(['POST', 'GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def ranking(request):
    dados = dict(request.data)
    rank = []
    try:
        Usuario.objects.get(user = request.user)
    except:
        return Response({"detail": "Usuário sem permissão"}, status=status.HTTP_400_BAD_REQUEST)
    usuarios = Usuario.objects.filter(admin=False)
    if request.method == 'POST': #verifica se existe a chave categoria para buscar por ela
        try:
            categoria = Categoria.objects.get(categoria_texto = dados["categoria"])
        except Categoria.DoesNotExist:
            return Response({"detail": "Informe uma categoria válida"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"detail": "Paramentros incorretos"}, status=status.HTTP_400_BAD_REQUEST)
        for u in usuarios:
            linha = []
            pontos = 0
            quizs = Quiz.objects.filter(usuario=u, perguntas__categoria=categoria)
            aux = []
            for q in quizs: #contar todos os pontos do usuario
                if q.id not in aux: #verificar se ja contou quiz
                    pontos += q.pontos
                    aux.append(q.id)
            linha.append(pontos)
            linha.append(u.user.username)
            rank.append(linha)
    else:
        for u in usuarios:
            linha = []
            pontos = 0
            quizs = Quiz.objects.filter(usuario=u)
            for q in quizs: #contar todos os pontos do usuario
                pontos += q.pontos
            linha.append(pontos)
            linha.append(u.user.username)
            rank.append(linha)
    rank = sorted(rank, key=lambda x : x[0])[::-1] #ordenando ranking
    json_rank = '{'
    for r in range(len(rank)):
        json_rank += f'\"{r+1}\":\"{rank[r][0]} - {rank[r][1]}\"{"" if r+1 == len(rank) else ","}'
    json_rank += '}'
    return Response(json.loads(json_rank))
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)
    
class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    permission_classes = (IsAuthenticated,)
class PerguntaViewSet(viewsets.ModelViewSet):
    serializer_class = PerguntaSerializer
    queryset = Pergunta.objects.all()
    permission_classes = (IsAuthenticated,)

class RespostaViewSet(viewsets.ModelViewSet):
    serializer_class = RespostaSerializer
    queryset = Resposta.objects.all()
    permission_classes = (IsAuthenticated,)

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    permission_classes = (IsAuthenticated,)

class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = (IsAuthenticated,)