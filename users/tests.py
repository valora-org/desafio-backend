from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from .models import User

user = {"email": "user@mail.com", "username": "user", "password": "123"}
admin = {"email": "admin@mail.com", "username": "admin", "password": "123"}


class RegisterViewTest(APITestCase):
    def test_create_account(self):
        response = self.client.post("/api/register/", user, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "user")

    def test_create_account_fail(self):

        response = self.client.post("/api/register/")

        self.assertEqual(response.status_code, 400)


class LoginViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_user(**user)

    def test_login(self):

        response = self.client.post("/api/login/", user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_fail(self):
        response = self.client.post("/api/login/")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

    def test_list_all_users(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_users_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_all_users_missing_token(self):
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserSingleViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

    def test_retrieve_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.get("/api/users/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/users/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_user_missing_token(self):
        response = self.client.get("/api/users/1/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RankingViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="1")
        self.user_token = user_token[0]

    def test_list_ranking(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/ranking/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_ranking_missing_token(self):
        response = self.client.get("/api/ranking/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
