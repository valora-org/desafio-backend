import uuid

from quiz import models

from . import base


class AnswerBaseTest(base.RestBaseTest):
    def setUp(self):
        super().setUp()

        self.question = self.create_fake_question(
            label="Question1", category=self.fake_category
        )
        self.pyload = {
            "label": f"Category {uuid.uuid4()}",
            "question": self.question.pk,
            "is_right": True,
        }


class AnswerTest(AnswerBaseTest):
    def test_create_returns_201(self):
        self.assertEquals(models.Answer.objects.count(), 0)

        self.auth(is_admin=True)
        response = self.client.post("/api/answers/", self.pyload)
        self.assertEquals(response.status_code, 201)

        self.assertEquals(models.Answer.objects.count(), 1)

        answer = models.Answer.objects.last()
        expected_data = {
            "id": answer.pk,
            "label": self.pyload["label"],
            "question": self.pyload["question"],
            "is_right": self.pyload["is_right"],
        }
        self.assertEquals(response.json(), expected_data)

    def test_detail_returns_200(self):
        answer = self.create_fake_answer(
            label="Resposta1", question=self.question, is_right=True
        )
        self.auth(is_admin=True)
        response = self.client.get(f"/api/answers/{answer.pk}/")
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": answer.pk,
            "label": answer.label,
            "question": self.question.pk,
            "is_right": True,
        }
        self.assertEquals(response.json(), expected_data)

    def test_list_returns_200(self):
        answer = self.create_fake_answer(
            label="Resposta1", question=self.question, is_right=True
        )
        self.auth(is_admin=True)
        response = self.client.get(f"/api/answers/")
        self.assertEquals(response.status_code, 200)

        expected_data = [
            {
                "id": answer.pk,
                "label": answer.label,
                "question": self.question.pk,
                "is_right": True,
            }
        ]
        self.assertEquals(response.json(), expected_data)

    def test_complete_update_returns_200(self):
        answer = self.create_fake_answer(
            label="Resposta1", question=self.question, is_right=True
        )
        payload = {
            "label": "Teste de respota1",
            "question": self.question.pk,
            "is_right": False,
        }

        self.auth(is_admin=True)
        response = self.client.put(f"/api/answers/{answer.pk}/", payload, format="json")
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": answer.pk,
            "label": payload["label"],
            "question": self.question.pk,
            "is_right": False,
        }
        self.assertEquals(response.json(), expected_data)

    def test_delete_returns_204(self):
        answer = self.create_fake_answer(
            label="Resposta1", question=self.question, is_right=True
        )

        self.auth(is_admin=True)
        response = self.client.delete(f"/api/questions/{answer.pk}/")
        self.assertEquals(response.status_code, 204)
