import random
import time

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
        response = self.client.get(reverse("users-detail", kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)


class QuizFlowTestCase(APITestCase):

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

    def test_search_category(self):
        data = {"search": "Mus"}
        response = self.client.get(reverse('category-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_questions(self):
        data = {"category": self.category['id']}
        questions = list()
        for item in range(1, 11):
            questions.append({"question": f"Pergunta {item}",
                              "answer": [
                                  {"answer": f"Responsta {item}.{anw}",
                                   "is_right": True if anw == 0 else False}
                                  for anw in range(0, 3)]
                              })
        data.update({"question": questions})
        response = self.client.post(reverse('question-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_quiz_flow(self):
        self.test_create_questions()  # Cria perguntas por categoria
        data = {
            "user": self.user.id,
            "category": int(self.category['id'])
        }

        # Adiciona perguntas no quiz por categoria
        response = self.client.post(reverse('quiz-list'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Response as perguntas de forma aleatoria, as respostas certas está sempre no indice 0
        data_quiz = response.data
        quiz_id = data_quiz['id']

        for question in data_quiz['questions'][:5]:
            data = {
                "question": question['id'],
                "answer": question['answer'][random.randint(0, 2)]
            }
            response = self.client.put(f"/api/quiz/{quiz_id}/", data=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(f"/api/quiz/{quiz_id}/finish/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
