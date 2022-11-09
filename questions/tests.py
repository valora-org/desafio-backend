from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from questions.models import Question
from users.models import User


user = {"email": "user@mail.com", "username": "user", "password": "123"}
admin = {"email": "admin@mail.com", "username": "admin", "password": "123"}


class QuestionViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

    def test_list_all_questions(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.get("/api/questions/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_questions_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/questions/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_question(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.post(
            "/api/questions/",
            data={
                "description": "New question",
                "answer": 1,
                "alternatives": [
                    {"description": "first alternative"},
                    {"description": "second alternative"},
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["id"], 1)

    def test_create_question_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.post(
            "/api/questions/",
            data={
                "description": "New question",
                "answer": 1,
                "alternatives": [
                    {"description": "first alternative"},
                    {"description": "second alternative"},
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class QuestionSingleViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

        Question.objects.create(description="New question", answer=1)

    def test_retrieve_question(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.get("/api/questions/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "question": {
                    "id": 1,
                    "description": "New question",
                    "alternatives": [],
                }
            },
        )

    def test_retrieve_question_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/questions/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_category(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.patch(
            "/api/questions/1/", data={"description": "New Question Name"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.data["question"].get("description"), "New Question Name"
        )

    def test_patch_category_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.patch(
            "/api/questions/1/", data={"name": "New Question Name"}
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_question(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.delete("/api/questions/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_question_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.delete("/api/questions/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
