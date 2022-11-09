from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User
from quizzes.models import Quiz
from categories.models import Category

user = {"email": "user@mail.com", "username": "user", "password": "123"}
admin = {"email": "admin@mail.com", "username": "admin", "password": "123"}


class QuizzViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

    def test_list_all_quizzes(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.get("/api/quizzes/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_quizzes_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/quizzes/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_quiz(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.post(
            "/api/quizzes/",
            data={
                "title": "New Quiz",
                "description": "New quiz",
                "categories": [{"name": "Category"}],
                "questions": [
                    {
                        "description": "Quiz Question",
                        "answer": 2,
                        "alternatives": [
                            {"description": "Quiz first alternative"},
                            {"description": "Quiz second alternative"},
                            {"description": "Quiz new third alternative"},
                        ],
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["id"], 1)

    def test_create_question_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.post(
            "/api/quizzes/",
            data={
                "title": "New Quiz",
                "description": "New quiz",
                "categories": [{"name": "Category"}],
                "questions": [
                    {
                        "description": "Quiz Question",
                        "answer": 2,
                        "alternatives": [
                            {"description": "Quiz first alternative"},
                            {"description": "Quiz second alternative"},
                            {"description": "Quiz new third alternative"},
                        ],
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class QuizSingleView(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

        Quiz.objects.create(title="Quiz", description="Quiz Description")

    def test_retrieve_quiz(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.get("/api/quizzes/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["quiz"].get("id"), 1)

    def test_retrieve_quiz_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/quizzes/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_quiz(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.patch("/api/quizzes/1/", data={"title": "New Quiz Name"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["quiz"].get("title"), "New Quiz Name")

    def test_patch_quiz_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.patch("/api/quizzes/1/", data={"title": "New Quiz Name"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_quiz(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.delete("/api/quizzes/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_quiz_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.delete("/api/quizzes/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GameViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

        quiz = Quiz.objects.create(title="Quiz", description="Quiz Description")
        category = Category.objects.create(name="category")
        quiz.categories.add(category)

    def test_get_game(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/play/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_game_not_loggedIn(self):
        response = self.client.get("/api/play/1/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_send_answer(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.post(
            "/api/play/1/", {"guesses": [{"question": 9, "guess": 2}]}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"quiz score": 0, "user score": 0})

    def test_send_answer_not_loggedIn(self):
        response = self.client.post("/api/play/1/", {"guesses": []}, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
