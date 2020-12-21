from django.urls import reverse

from quiz.models import Category
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User, Group


class CategoryTests(APITestCase):

    def setUp(self):
        self.group = Group.objects.create(name="Player")
        self.user = User.objects.create_user(username='testuser', email='testuser@test.com', password='testing')
        token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_transactions(self):
        dto = {
            "description": "first",
            "value": 10
        }

        response = self.client.post(reverse('transactions'), dto, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_cant_create_transaction_with_value_0(self):
        dto = {
            "description": "first",
            "value": 0
        }

        response = self.client.post(reverse('transactions'), dto, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 0)