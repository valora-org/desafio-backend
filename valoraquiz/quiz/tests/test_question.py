import uuid

from quiz import models

from . import base


class QuestionBaseTest(base.RestBaseTest):
    def setUp(self):
        super().setUp()
        self.payload = {
            "label": f"Question {uuid.uuid4()}",
            "category": self.fake_category.pk,
        }


class QuestionTest(QuestionBaseTest):
    def test_create_returns_201(self):
        self.assertEquals(models.Question.objects.count(), 0)

        self.auth(is_admin=True)
        response = self.client.post("/api/questions/", self.payload)
        self.assertEquals(response.status_code, 201)

        self.assertEquals(models.Question.objects.count(), 1)

        question = models.Question.objects.first()
        expected_data = {
            "id": question.pk,
            "label": self.payload["label"],
            "category": self.payload["category"],
        }
        self.assertEquals(response.json(), expected_data)

    def test_detail_returns_200(self):
        question = self.create_fake_question(
            label="Question1", category=self.fake_category
        )

        self.auth(is_admin=True)
        response = self.client.get(f"/api/questions/{question.pk}/")
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": question.pk,
            "label": question.label,
            "category": question.category.pk,
        }
        self.assertEquals(response.json(), expected_data)

    def test_detail_returns_404(self):

        self.auth(is_admin=True)
        response = self.client.get(f"/api/questions/1/")
        self.assertEquals(response.status_code, 404)

    def test_list_returns_200(self):
        question = self.create_fake_question(
            label="Question1", category=self.fake_category
        )

        self.auth(is_admin=True)
        response = self.client.get(f"/api/questions/")
        self.assertEquals(response.status_code, 200)

        expected_data = [
            {
                "id": question.pk,
                "label": question.label,
                "category": question.category.pk,
            }
        ]
        self.assertEquals(response.json(), expected_data)

    def test_complete_update_returns_200(self):
        question = self.create_fake_question(
            label="Question1", category=self.fake_category
        )
        payload = {
            "label": "How to install django?",
            "category": self.create_fake_category(title="How-to").pk,
        }

        self.auth(is_admin=True)
        response = self.client.put(
            f"/api/questions/{question.pk}/", payload, format="json"
        )
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": question.pk,
            "label": payload["label"],
            "category": payload["category"],
        }
        self.assertEquals(response.json(), expected_data)

    def test_partial_update_returns_200(self):
        question = self.create_fake_question(
            label="Question1", category=self.fake_category
        )
        payload = {
            "label": "How to install django?",
        }

        self.auth(is_admin=True)
        response = self.client.patch(
            f"/api/questions/{question.pk}/", payload, format="json"
        )
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": question.pk,
            "label": payload["label"],
            "category": question.category.pk,
        }
        self.assertEquals(response.json(), expected_data)

    def test_delete_returns_204(self):
        question = self.create_fake_question(
            label="Question1", category=self.fake_category
        )

        self.auth(is_admin=True)
        response = self.client.delete(f"/api/questions/{question.pk}/")
        self.assertEquals(response.status_code, 204)
