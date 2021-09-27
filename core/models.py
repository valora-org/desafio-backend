from annoying.fields import AutoOneToOneField
from django.db import models
from django.contrib.auth.models import User
import random

class Usuario(models.Model):
  user = AutoOneToOneField(User, on_delete=models.CASCADE, related_name="usuario")
  admin = models.BooleanField(default=False)
  
  def __str__(self):
        return self.user.username
  
class Pergunta(models.Model):
  pergunta_texto = models.CharField(max_length=200)
  categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
  
  def __str__(self):
        return self.pergunta_texto
  
class Quiz(models.Model):
  usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
  perguntas = models.ManyToManyField(Pergunta)
  questao_respondida = models.IntegerField(default= 0)
  pontos = models.IntegerField(default= 0)
  
  def __str__(self):
        return self.usuario.user.username
  '''
  Metodo responsavel para criar quiz
  usuario_play: usuario
  categoria_play: texto da categoria
  retorna: quiz
  '''
  def criar(usuario_play, categoria_play):
    quiz = Quiz.objects.create(usuario=usuario_play)
     
    perguntas_todas = Pergunta.objects.filter(categoria__categoria_texto=categoria_play)
    for p in range(10): #buscar 10 perguntas da categoria
      pergunta = random.choice(perguntas_todas) #buscar de forma aleatoria
      quiz.perguntas.add(pergunta.id)
      perguntas_todas = perguntas_todas.exclude(id = pergunta.id) #evitar que a pergunta seja repetida
        
    return quiz
  
  '''
  Metodo responsavel para iniciar o quiz
  usuario_play: usuario
  retorna: pergunta, lista de alternativas
  '''
  def play(usuario_play):
    try:
      quiz = Quiz.objects.get(usuario=usuario_play, questao_respondida__lt = 10) #buscar o ultimo quiz com menos de 10 perguntas respondidas
    except:
      return None, None
    perguntas = quiz.perguntas.all().order_by('id')
    pergunta = perguntas[quiz.questao_respondida] # ultima pergunta nao respondida
    alternativas_todas = Resposta.objects.filter(pergunta = pergunta)
    alternativas = []
    for r in range(3): #buscar as 3 alternativas
      alternativa = random.choice(alternativas_todas) #buscar de forma aleatoria
      alternativas.append(alternativa.resposta_texto)
      alternativas_todas = alternativas_todas.exclude(id = alternativa.id) #evitar que a resposta seja repetida
    
    return pergunta, alternativas
  
  '''
  Metodo responsavel para checar se a resposta esta correta
  usuario_play: usuario
  resposta: texto da resposta
  retorna: True/False
  '''
  def verificar(usuario_play, resposta):
    try:
      quiz = Quiz.objects.get(usuario=usuario_play, questao_respondida__lt = 10) #buscar o ultimo quiz com menos de 10 perguntas respondidas
    except:
      return None
    perguntas = quiz.perguntas.all().order_by('id')
    pergunta = perguntas[quiz.questao_respondida] #ultima pergunta que acabou de ser respondida
    try:
      acertou = Resposta.objects.get(pergunta = pergunta, resposta_texto = resposta).correta #verifica se a resposta foi correta
    except:
      return None
    if acertou: #se acertou somo +1 para a pontuacao
      quiz.pontos += 1
    else:
      if quiz.pontos != 0: #se errou -1 na pontuacao se for diferente de 0, sendo 0 a pontuacao minima
        quiz.pontos -= 1
    quiz.questao_respondida += 1 #marca que a pergunta foi respondida
    quiz.save()
    
    return acertou
 
class Resposta(models.Model):
  resposta_texto = models.CharField(max_length=200)
  correta = models.BooleanField(default=False)
  pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
  
  def __str__(self):
        return f'{self.pergunta.pergunta_texto} - {self.resposta_texto} - Correto: {self.correta}'

class Categoria(models.Model):
  categoria_texto = models.CharField(max_length=200)
  
  def __str__(self):
        return self.categoria_texto
  
