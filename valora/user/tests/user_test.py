from django.contrib.auth.models import User
from django.urls import reverse
# variáveis globais
from rest_framework.test import APITestCase

username = "usuariotest"
password = "senha123msa"
email = "albertow@gmail.com"


class UserTestCase(APITestCase):
    def setUp(self):
        url = reverse('rest_register')
        headers = {"username": username, "email": email, "password1": password,
                   "password2": password}
        self.response = self.client.post(url, headers)
        self.token = "Token %s " % self.response.json()["key"]

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 201)

    def test_models_user(self):
        self.assertEquals(User.objects.all().count(), 1)
        self.assertEquals(User.objects.all()[0].username, username)
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_login(self):
        url = reverse('rest_login')
        headers = {"username": username, "password": password, }
        self.response = self.client.post(url, headers)
        self.assertEquals(self.response.status_code, 200)

    def test_logout(self):
        url = reverse('rest_logout')
        headers = {'Authorization': self.token}
        self.response = self.client.post(url, headers)
        self.assertEquals(self.response.status_code, 200)


class InvalidPasswordResetTests(APITestCase):

    def setUp(self):
        url = reverse('rest_register')
        headers = {"username": username, "email": email, "password1": password,
                   "password2": password}
        self.response = self.client.post(url, headers)
        self.token = "Token %s " % self.response.json()["key"]

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 201)

    def test_login(self):
        url = reverse('rest_login')
        headers = {"username": username, "password": "password", }
        self.response = self.client.post(url, headers)
        self.assertEquals(self.response.status_code, 400)
