from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Usuario, Pergunta, Resposta, Categoria
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient



# Create your tests here.
class FluxoPrincipalTestes(TestCase):
  def setup(self):
    #criar usuario play
    usuario_play = User.objects.create(username="bob")
    usuario_play.set_password("naotemsenha123")
    usuario_play.save()
    Token.objects.create(user = usuario_play)
    Usuario.objects.create(user = usuario_play)
    
    #criar usuario admin
    usuario_admin = User.objects.create(username="alice")
    usuario_admin.set_password("naotemsenha123")
    usuario_admin.save()
    Token.objects.create(user = usuario_admin)
    Usuario.objects.create(user = usuario_admin, admin = True)
    
    #criar pergunta com categoria e resposta
    categoria = Categoria.objects.create(categoria_texto = 'esporte')
    for i in range(12):
      pergunta = Pergunta.objects.create(pergunta_texto = "Qual foram os Brasileios eleitos Melhores do Mundo?", categoria = categoria)
      Resposta.objects.create(pergunta = pergunta, resposta_texto = "Friesdenrei,Agostinho Fortes,Domingos da Guia,Pelé,Ronaldo,Rivaldo,Adriano e Robinho", correta = True)
      Resposta.objects.create(pergunta = pergunta, resposta_texto = "Ronaldo,Rivaldo,Adriano e Robinho")
      Resposta.objects.create(pergunta = pergunta, resposta_texto = "Pelé,Ronaldo,Rivaldo,Adriano e Robinho")
    
  
  '''
  Teste da criacao de pergunta
  '''
  def test_criar_pergunta(self):
    self.setup()
    usuario = User.objects.get(username="alice")  
    data = {"pergunta": "Qual foram os Brasileios eleitos Melhores do Mundo?",
            "categoria": "esporte",
            "alternativa_correta": "Friesdenrei,Agostinho Fortes,Domingos da Guia,Pelé,Ronaldo,Rivaldo,Adriano e Robinho",
            "alternativa1": "Ronaldo,Rivaldo,Adriano e Robinho",
            "alternativa2": "Pelé,Ronaldo,Rivaldo,Adriano e Robinho"}
    
    url = '/perguntas/'
    cliente = APIClient()
    cliente.credentials(HTTP_AUTHORIZATION='Token ' + str(usuario.auth_token))
    request = cliente.post(url, data=data)
    self.assertQuerysetEqual(str(request.status_code), '201') 
  
  '''
  Teste do fluxo de criar quiz, consultar pergunta, responder e obter ranking
  '''
  def test_criar_quiz_e_jogar(self):
    self.setup()
    usuario = User.objects.get(username="bob")  
    cliente = APIClient()
    cliente.credentials(HTTP_AUTHORIZATION='Token ' + str(usuario.auth_token))
    request1 = cliente.post('/', data={'categoria': 'esporte'})
    request2 = cliente.get('/play/')
    self.assertQuerysetEqual(str(request1.status_code), '201')
    self.assertQuerysetEqual(str(request2.status_code), '200')
    for i in range(10):
      request3 = cliente.post('/resposta/', data={"resposta": "Friesdenrei,Agostinho Fortes,Domingos da Guia,Pelé,Ronaldo,Rivaldo,Adriano e Robinho"})
      self.assertQuerysetEqual(str(request3.status_code), '200')
      self.assertQuerysetEqual(str(request3.data),"{'Resposta: CERTA'}")
    request3 = cliente.get('/ranking/')
    self.assertQuerysetEqual(str(request3.status_code), '200')
    
    