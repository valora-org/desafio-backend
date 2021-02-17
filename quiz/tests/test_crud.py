from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from quiz.models import Category


class APITests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.test_user = User.objects.create_user(
            "testuser", "test@test.com", "testpass"
        )
        self.test_admin = User.objects.create_user(
            "testadmin", "teste@teste.com", "testeadminpass"
        )
        self.test_admin.type = User.ADMIN
        self.test_admin.save()

        self.test_category = Category(
            slug="teste", name="categoria teste"
        )
        self.test_category.save()
        self.valid_user = {
            "username": "testuser",
            "password": "testpass"
        }
        self.valid_admin_user = {
            "username": "testadmin",
            "password": "testeadminpass"
        }
        self.invalid_user = {
            "username": "t",
            "password": "s"
        }
        self.valid_question = {
            "answers": [
                {"text": "resposta 2", "is_right": True},
                {"text": "resposta 3", "is_right": False},
                {"text": "resposta 4", "is_right": False}
            ],
            "title": "Pergunta t?",
            "category": self.test_category.id
        }
        self.auth_url = reverse('get-token')
        self.questions_url = reverse('question-list')
        self.game_url = reverse('game-list')

    def test_authentication(self):
        # valid credentials
        response = self.client.post(self.auth_url, self.valid_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data.keys())

        # invalid credentials
        response = self.client.post(self.auth_url, self.invalid_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('non_field_errors' in response.data.keys())

    def test_create_unauthenticated(self):
        # no token
        response = self.client.post(self.questions_url, self.valid_question)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue('detail' in response.data.keys())

        # invalid token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer Token')
        response = self.client.post(self.questions_url, self.valid_question)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue('detail' in response.data.keys())

    def test_create_authenticated_user(self):
        # usuario comum
        response_auth = self.client.post(self.auth_url, self.valid_user)
        token = response_auth.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.questions_url, self.valid_question,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_authenticated_admin(self):
        # usuario admin
        response_auth = self.client.post(self.auth_url, self.valid_admin_user)
        token = response_auth.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.questions_url, self.valid_question,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_game(self):
        response_auth = self.client.post(self.auth_url, self.valid_user)
        token = response_auth.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(self.game_url, {},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('category' in response.data.keys())

        response = self.client.post(self.game_url, {"category": "teste"},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in response.data.keys())
        self.assertTrue('questions' in response.data.keys())
