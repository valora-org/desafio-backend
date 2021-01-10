from django.contrib.auth.models import User
from django.urls import reverse
from model_mommy import mommy
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from quiz.models import Category

# variáveis globais
adminUsername = "admintest"
adminPassword = "senha123msa"
username = "usuariotest"
password = "senha123msa"
email = "albertow@gmail.com"


class UserPesmissionsTestCase(APITestCase):
    # Teste com usuário comum
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username=username, email=email, password=password)
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # Somente o usuário logado tem assessor ao ranking
    def test_ranking(self):

        self.response = self.client.get(reverse('user:ranking'))
        self.assertEquals(self.response.status_code, 200)

    # Somente o usuário adm logado tem assessor a categorias [PUT,POST,GET,DELETE]

    def teste_categorias(self):
        self.response = self.client.get(reverse('quiz:question-adm'))
        self.assertEquals(self.response.status_code, 403)
        self.assertEquals(self.response.json()["detail"], 'You do not have permission to perform this action.')

    # Somente o usuário adm logado tem assessor as questões [PUT,POST,GET,DELETE]

    def teste_questoes(self):
        self.response = self.client.get(reverse('quiz:category-adm'))
        self.assertEquals(self.response.status_code, 403)
        self.assertEquals(self.response.json()["detail"], 'You do not have permission to perform this action.'),

    # Somente o usuário logado tem assessor ao quiz
    def test_start_quiz(self):
        self.category = mommy.make(Category)
        self.response = self.client.get(reverse('quiz:start', kwargs={'category_id': self.category.id}), )
        self.assertEquals(self.response.status_code, 200)

    # Somente o usuário logado tem assessor a lista de categorias
    def test_lista_de_categorias(self):
        self.response = self.client.get(reverse('quiz:category_list'))
        self.assertEquals(self.response.status_code, 200)


class UserPesmissionsAdmTestCase(APITestCase):
    # Teste com usuário admin
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username=username, email=email, password=password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.response = self.client.get(reverse('quiz:question-adm'))

    # Somente o usuário adm logado tem assessor a categorias [PUT,POST,GET,DELETE]

    def teste_categorias(self):
        self.client.force_login(user=self.user)
        self.assertEquals(self.response.status_code, 200)

    # Somente o usuário adm logado tem assessor as questões [PUT,POST,GET,DELETE]
    def teste_questoes(self):
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.response = self.client.get(reverse('quiz:category-adm'))
        self.assertEquals(self.response.status_code, 200)


class UserNotPesmissionsTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    # Somente o usuário logado tem assessor ao ranking "Poderia fazer mais teste posteriomente"
    def test_ranking_sem_user_logado(self):
        self.response = self.client.get(reverse('user:ranking'))
        self.assertEquals(self.response.status_code, 401)
        self.assertEquals(self.response.json()["detail"], 'Authentication credentials were not provided.')