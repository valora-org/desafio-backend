
import re
import pytest
from model_bakery import baker
from rest_framework.test import APITestCase

from quizzes.models import Answer, Question, Ranking


@pytest.mark.django_db
class TestAnswerView(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        admin = baker.make("users.User", username="Joao", is_admin=True)
        player = baker.make("users.User", username="Marcos", is_admin=False)
        question = baker.make("quizzes.Question")
        self.data = {
            "admin": admin,
            "player": player,
            "question": question,
        }

    def test_authentication_on_endpoints(self):
        data = {"answers": [
                {"text": "Text 1",
                 "question": self.data["question"].id, "is_correct": False},
                {"text": "Text 2",
                 "question": self.data["question"].id, "is_correct": True},
                {"text": "Text 3",
                 "question": self.data["question"].id, "is_correct": False}
                ]
                }

        # Make request without any user authenticated
        response = self.client.post(
            "/api/answer/", data=data, format="json"
        )

        assert response.status_code == 401

        # Make request with player who has no permission to the endpoint
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.post(
            "/api/answer/", data=data, format="json"
        )

        assert response.status_code == 403

        response = self.client.get(
            "/api/answers/", data=data, format="json"
        )

        assert response.status_code == 403

        # Test missing data on create payload
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.post(
            "/api/answer/", data={}, format="json"
        )
        assert response.status_code == 400

        # Test admin has permission to create and update answer
        response = self.client.post(
            "/api/answer/", data=data, format="json"
        )
        assert response.status_code == 201
        assert Answer.objects.count() == 3
        assert Answer.objects.filter(
            text="Text 1", question=self.data["question"], is_correct=False).exists()
        assert Answer.objects.filter(
            text="Text 2", question=self.data["question"], is_correct=True).exists()
        assert Answer.objects.filter(
            text="Text 3", question=self.data["question"], is_correct=False).exists()

        answer = Answer.objects.filter(text="Text 3").get()

        data = {"text": "Text 4"}
        response = self.client.put(
            f"/api/answer/{answer.id}/", data=data, format="json"
        )

        assert response.status_code == 200
        assert Answer.objects.count() == 3
        assert Answer.objects.filter(
            text="Text 4", question=self.data["question"], is_correct=False).exists()

        # Test missing data on update payload
        response = self.client.put(
            f"/api/answer/{answer.id}/", data={}, format="json"
        )
        assert response.status_code == 400
        assert response.data == "Missig field."

        # Test player can't update answer's text
        data = {"text": "Text 3"}
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.put(
            f"/api/answer/{answer.id}/", data=data, format="json"
        )

        assert response.status_code == 403
        assert Answer.objects.filter(
            text="Text 4", question=self.data["question"], is_correct=False).exists()
        assert not Answer.objects.filter(
            text="Text 3", question=self.data["question"], is_correct=False).exists()

        # Test player can't delete answer
        response = self.client.delete(
            f"/api/answer/{answer.id}/", data=data, format="json"
        )

        assert response.status_code == 403
        assert Answer.objects.count() == 3

        # Test admin can delete answer
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.delete(
            f"/api/answer/{answer.id}/", data=data, format="json"
        )

        assert response.status_code == 204
        assert Answer.objects.count() == 2


@pytest.mark.django_db
class TestQuestionView(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        admin = baker.make("users.User", username="Andre", is_admin=True)
        player = baker.make("users.User", username="Renato", is_admin=False)
        category = baker.make("categories.Category", name="Sport")
        self.data = {
            "admin": admin,
            "player": player,
            "category": category
        }

    def test_authentication_on_endpoints(self):
        data = {"text": "Text", "category": self.data["category"].id}

        # Make request without any user authenticated
        response = self.client.post(
            "/api/question/", data=data, format="json"
        )

        assert response.status_code == 401

        # Make request with player who has no permission to the endpoint
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.post(
            "/api/question/", data=data, format="json"
        )

        assert response.status_code == 403

        response = self.client.get(
            "/api/questions/", data=data, format="json"
        )

        assert response.status_code == 403

        # Test missing data on create payload
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.post(
            "/api/question/", data={}, format="json"
        )
        assert response.status_code == 400

        # Test admin has permission to create and update question
        response = self.client.post(
            "/api/question/", data=data, format="json"
        )
        assert response.status_code == 201
        assert Question.objects.count() == 1
        assert Question.objects.last().text == "Text"
        assert Question.objects.last().category == self.data["category"]

        question = Question.objects.last()

        data = {"text": "New Text"}
        response = self.client.put(
            f"/api/question/{question.id}/", data=data, format="json"
        )

        assert response.status_code == 200
        assert Question.objects.count() == 1
        assert Question.objects.last().text == "New Text"
        assert Question.objects.last().category == self.data["category"]

        # Test missing data on update payload
        response = self.client.put(
            f"/api/question/{question.id}/", data={}, format="json"
        )
        assert response.status_code == 400
        assert response.data == "Missig field."

        # Test player can't update question's text
        data = {"text": "Text"}
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.put(
            f"/api/question/{question.id}/", data=data, format="json"
        )

        assert response.status_code == 403
        assert Question.objects.last().text == "New Text"

        # Test player can't delete question
        response = self.client.delete(
            f"/api/question/{question.id}/", data=data, format="json"
        )

        assert response.status_code == 403
        assert Question.objects.count() == 1

        # Test admin can delete question
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.delete(
            f"/api/question/{question.id}/", data=data, format="json"
        )

        assert response.status_code == 204
        assert Question.objects.count() == 0


@pytest.mark.django_db
class TestGetQuizView(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        admin = baker.make("users.User", username="Joao", is_admin=True)
        player = baker.make("users.User", username="Marcos", is_admin=False)
        category_1 = baker.make("categories.Category", name="Sport")
        category_2 = baker.make("categories.Category", name="Clothes")

        same_category_questions = baker.make(
            "quizzes.Question", _quantity=20, category=category_1)
        for question in same_category_questions:
            baker.make("quizzes.Answer", question=question, is_correct=True)
            baker.make("quizzes.Answer", question=question,
                       is_correct=False, _quantity=2)

        different_category_questions = baker.make(
            "quizzes.Question", category=category_2)
        baker.make("quizzes.Answer",
                   question=different_category_questions, is_correct=True)
        baker.make("quizzes.Answer", question=different_category_questions,
                   is_correct=False, _quantity=2)
        self.data = {
            "admin": admin,
            "player": player,
            "category_1": category_1,
            "category_2": category_2,
        }

    def test_send_quiz_with_random_questions(self):
        # Test request without authentication
        response = self.client.get(
            "/api/get-quiz/", data={}, format="json"
        )
        assert response.status_code == 401

        # Test missing data on list payload
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.get(
            "/api/get-quiz/"
        )
        assert response.status_code == 400

        # Test invalid data on list payload
        response = self.client.get(
            "/api/get-quiz/", data={"category": "Environment"}, format="json"
        )
        assert response.status_code == 400

        # Test return random questions
        response = self.client.get(
            "/api/get-quiz/", data={"category": self.data["category_1"].name}, format="json"
        )
        assert response.status_code == 200
        assert len(response.data) == 10
        assert 'answers' in response.data[0]
        assert len(response.data[0]['answers']) == 3

        first_quiz = response.data

        response = self.client.get(
            "/api/get-quiz/", data={"category": self.data["category_1"].name}, format="json"
        )

        second_quiz = response.data

        assert first_quiz != second_quiz


@pytest.mark.django_db
class TestRankingView(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        admin = baker.make("users.User", username="Joao", is_admin=True)
        player = baker.make("users.User", username="Marcos", is_admin=False)
        category_1 = baker.make("categories.Category", name="Sport")
        category_2 = baker.make("categories.Category", name="Cars")

        same_category_questions = baker.make(
            "quizzes.Question", _quantity=10, category=category_1)
        for question in same_category_questions:
            baker.make("quizzes.Answer", question=question, is_correct=True)
            baker.make("quizzes.Answer", question=question,
                       is_correct=False, _quantity=2)

        different_category_questions = baker.make(
            "quizzes.Question", category=category_2)
        baker.make("quizzes.Answer",
                   question=different_category_questions, is_correct=True)
        baker.make("quizzes.Answer", question=different_category_questions,
                   is_correct=False, _quantity=2)

        self.data = {
            "admin": admin,
            "player": player,
            "category_1": category_1,
            "category_2": category_2,
        }

    def test_authentication_and_response_on_endpoints(self):
        valid_answer_ids_1 = Answer.objects.filter(question__category=self.data["category_1"]).distinct(
            "question").values_list("id", flat=True)[:10]
        valid_answer_ids_2 = [id+1 for id in valid_answer_ids_1]
        invalid_answer_ids = Answer.objects.filter(question__category=self.data["category_2"]).distinct(
            "question").values_list("id", flat=True)[:1]

        valid_data_1 = {"ids": valid_answer_ids_1}
        valid_data_2 = {"ids": valid_answer_ids_1[:7] + valid_answer_ids_2[:3]}

        assert valid_data_1 != valid_data_2

        invalid_data_incorrect_amount = {"ids": list(valid_answer_ids_1[:9])}
        invalid_data_different_categories = {"ids": list(
            valid_answer_ids_1[:9]) + list(invalid_answer_ids)}

        # Make request without any user authenticated
        response = self.client.post(
            "/api/finish-quiz/", data=valid_data_1, format="json"
        )

        assert response.status_code == 401

        # Make request with player and admin to the endpoint
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.post(
            "/api/finish-quiz/", data=valid_data_1, format="json"
        )

        assert response.status_code == 201
        assert response.data["global_rank"] == 1
        assert response.data["score"] == 10

        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.post(
            "/api/finish-quiz/", data=valid_data_1, format="json"
        )
        assert response.status_code == 201
        assert response.data["global_rank"] == 2
        assert response.data["score"] == 10

        response = self.client.post(
            "/api/finish-quiz/", data=valid_data_2, format="json"
        )
        assert response.status_code == 201
        assert response.data["global_rank"] == 3
        assert response.data["score"] == 4

        self.client.force_authenticate(user=self.data["player"])
        response = self.client.post(
            "/api/finish-quiz/", data=valid_data_1, format="json"
        )
        assert response.status_code == 201
        assert response.data["global_rank"] == 3
        assert response.data["score"] == 10

        # Test list ranking without category
        response = self.client.get(
            "/api/ranking/", data={}, format="json"
        )

        assert response.status_code == 200
        assert response.data[2]['user'] == self.data["player"].id
        assert response.data[3]['user'] == self.data["admin"].id

        # Test list ranking with invalid category
        response = self.client.get(
            "/api/ranking/", data={"category": "Text"}, format="json"
        )

        assert response.status_code == 400

        # Test list ranking with valid category
        response = self.client.get(
            "/api/ranking/", data={"category": self.data["category_2"].name}, format="json"
        )

        assert response.status_code == 200
        assert len(response.data) == 0

        response = self.client.get(
            "/api/ranking/", data={"category": self.data["category_1"].name}, format="json"
        )

        assert response.status_code == 200
        assert len(response.data) == 4

        # Test missing data on payload
        response = self.client.post(
            "/api/finish-quiz/", data={}, format="json"
        )

        assert response.status_code == 400
        assert response.data == "Missing answers."

        # Test invalid data on payloads
        response = self.client.post(
            "/api/finish-quiz/", data=invalid_data_incorrect_amount, format="json"
        )

        assert response.status_code == 400
        assert response.data == "Invalid payload. Not enought questions answered"

        response = self.client.post(
            "/api/finish-quiz/", data=invalid_data_different_categories, format="json"
        )

        assert response.status_code == 400
        assert response.data == "Answers are from questions of different categories."
