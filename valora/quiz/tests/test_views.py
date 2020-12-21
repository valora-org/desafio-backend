from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import Group, User


class RegistrationTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

    def test_registration(self):
        print("test_registration")
        Group.objects.update_or_create(name="Player")
        client = APIClient()

        # Admin token
        client.credentials(HTTP_AUTHORIZATION='Token 483325994134d5baf0e303d938a0756d4ec4fb83')

        data = {"username": "user_test2", "password1": "MOMOeang", "password2": "MOMOeang"}
        response = self.client.post("/rest_auth/registration/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category(self):
        print("test_category")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_id(self):
        print("test_category_id")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/category/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question(self):
        print("test_question")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/question/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_id(self):
        print("test_question_id")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/question/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_category(self):
        print("test_question_category")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/question/category/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_answer(self):
        print("test_answer")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/answer/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_answer_author(self):
        print("test_answer_author")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/answer/author/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ranking(self):
        print("test_ranking")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/ranking/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ranking_category(self):
        print("test_ranking_category")
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/api/ranking/category/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
