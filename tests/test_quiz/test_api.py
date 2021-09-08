from rest_framework import status
from rest_framework.test import APITestCase
from quiz.models import User
from tests.conftest import URL

class UserTests(APITestCase):
    def test_check_user(self):
        route = '/api/user/'
        user = User.objects.create_user('valora', 'Pas$w0rd')
        self.client.force_authenticate(user)
        response = self.client.get(URL + route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_1(self):
        route = '/api/user/'
        data = {
            'username': 'Test',
            'admin': 'False'
        }
        response = self.client.post(URL + route, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_2(self):
        user = User.objects.create_user('Test', 'Pas$w0rd', admin=True)
        user.save()
        user.refresh_from_db()
        # self.client.login(username='Test', password='Pas$w0rd')
        self.client.force_authenticate(user)

        route = '/api/user/'
        data = {
            'id': 1,
            'username': 'Vampire',
            'admin': 'False'
        }

        response = self.client.post(URL + route, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username='Vampire').username, 'Vampire')
        self.assertEqual(User.objects.get(username='Vampire').admin, False)