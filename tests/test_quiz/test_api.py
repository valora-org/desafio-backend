from django.urls import reverse_lazy, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from quiz.models import User
from tests.conftest import URL

class AccountTests(APITestCase):
    def test_check_user(self):
        route = '/api/user/'
        user = User.objects.create_user('test', 'Pas$w0rd')
        self.assertTrue(self.client.login(username='test', password='Pas$w0rd'))
        response = self.client.get(URL + route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        # Necessário logar para acessar
        route = '/api/user/'
        data = {
            'id' : 6,
            'username': 'Test',
            'admin': 'False'
        }
        response = self.client.post(URL + route, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Test')
        self.assertEqual(User.objects.get().admin, 'False')

    # def test_create_account(self):
    #     url = reverse('api/quiz')
    #     data = {
    #         'category': 'Music',
    #         'user': 'test'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Quiz.objects.count(), 1)
    #     self.assertEqual(Quiz.objects.get().category, 'Music')