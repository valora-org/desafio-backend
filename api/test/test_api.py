from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import User, Quiz


class UsersTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(username="admin",
                                              email='admin@gmail.com',
                                              password='1234!@#$')
        self.api_authentication()

    def api_authentication(self):
        url = reverse('token_obtain_pair')
        data = {
            "username": "admin@gmail.com",
            "password": "1234!@#$"
        }
        response = self.client.post(url, data, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_user_auth(self):
        response = self.client.get(reverse("users-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_un_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse("users-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_detail_retrieve(self):
        response = self.client.get(reverse("users-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)


class QuizTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects._create_user(username="admin",
                                              email='admin@gmail.com',
                                              password='1234!@#$')
        self.api_authentication()
        self.category = self.create_category()

    def api_authentication(self):
        url = reverse('token_obtain_pair')
        data = {
            "username": "admin@gmail.com",
            "password": "1234!@#$"
        }
        response = self.client.post(url, data, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def create_category(self):
        data = {"description": "Musical"}
        response = self.client.post(reverse("category-list"), data=data, format='json')
        return response.data

    def test_create_quiz(self):
        data = {"name": "Meu Quiz", "category": self.category['id']}
        questions = list()
        for item in range(1, 11):
            questions.append({"question": f"Pergunta {item}",
                              "answer": [
                                  {"answer": f"Responsta {item}.{anw}",
                                   "is_right": True if anw == 0 else False}
                                  for anw in range(0, 3)]
                              })
        data.update({"question": questions})
        response = self.client.post(reverse('quiz-list'), data,  format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

