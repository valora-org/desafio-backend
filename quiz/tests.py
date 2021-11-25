from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FluxoPrincipalTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(username="admin",
                                              email="admin@admin.com",
                                          password='1234',
                                          is_staff=True)
        self.logar()
    def logar(self):
        url = reverse('get-token')
        response = self.client.post(url,{"username":"admin","password":"1234"},format="json")
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

    def test_criarQuestao(self):
        url = reverse('questao-list')
        data = {"texto":"Pergunta TesteCase","categoria":1}
        response = self.client.post(url,data,format="json")
        print(response, "************88")
        self.idJogo =response.data['data']['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_iniciarJogo(self):
        url = reverse('iniciar-jogo')
        data = {"categoria":1}
        response = self.client.post(url,data,format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_finalizarJogo(self):
        url = f'/finalizar-jogo/{self.idJogo}'
        data = {"respostas":[{}]}
        response = self.client.put(url,data,format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verRanking(self):
        url = reverse('ranking-global')
        response = self.client.get(url,data=None,format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
