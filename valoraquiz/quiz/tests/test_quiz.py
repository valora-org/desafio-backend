from quiz import models, services

from . import base


class QuizBaseTest(base.RestBaseTest):
    def setUp(self):
        super().setUp()

        self.category = self.create_fake_category(title="Category1")
        self.payload = {"category_id": self.category.pk}
        self.category_without_questions = self.create_fake_category(title="Category2")

    def build_questions(self, category):
        count = 0
        while count <= 10:
            question = self.create_fake_question(
                label=f"Question {count}", category=category
            )
            for idx in range(3):
                self.create_fake_answer(
                    label=f"Answer {idx}",
                    question=question,
                    is_right=False if idx < 2 else True,
                )
            count += 1


class QuizTest(QuizBaseTest):
    def test_create_returns_201(self):
        self.build_questions(self.category)
        self.assertEquals(models.Quiz.objects.count(), 0)

        self.auth()
        response = self.client.post("/api/quizzes/", self.payload)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(models.Quiz.objects.count(), 1)

        quiz = models.Quiz.objects.last()
        expected_data = {
            "id": quiz.pk,
            "category_id": self.category.pk,
            "is_finished": False,
            "questions": [
                {
                    "id": question.pk,
                    "label": question.label,
                    "category_id": question.category_id,
                    "answers_available": [
                        {
                            "id": answer_available.pk,
                            "label": answer_available.label,
                            "is_right": answer_available.is_right,
                        }
                        for answer_available in question.answer_set.all()
                    ],
                }
                for question in quiz.questions.all()
            ],
            "answers": [],
        }
        self.assertDictEqual(response.json(), expected_data)

    def test_create_with_invalid_category_returns_400(self):
        self.assertEquals(models.Quiz.objects.count(), 0)

        payload = {"category_id": self.category_without_questions.pk}

        self.auth()
        response = self.client.post("/api/quizzes/", payload)
        self.assertEquals(response.status_code, 400)

        self.assertEquals(models.Quiz.objects.count(), 0)

        expected_error = {"error": "This category has no 10 questions"}
        self.assertEquals(response.json(), expected_error)

    def test_answered_quiz_returns_200(self):
        category = self.create_fake_category(title="Filmes")
        self.build_questions(category)

        quiz = services.create_quiz(category_id=category.pk, user=self.user_player)

        data = {
            "answers": [
                {
                    "question_id": question.pk,
                    "answer_id": (question.answer_set.all().order_by("?").first().pk),
                }
                for question in quiz.questions.all()
            ],
            "is_finished": True,
        }

        self.auth()
        response = self.client.patch(f"/api/quizzes/{quiz.pk}/", data, format="json")
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": quiz.pk,
            "category_id": category.pk,
            "is_finished": data["is_finished"],
            "questions": [
                {
                    "id": question.pk,
                    "label": question.label,
                    "category_id": question.category_id,
                    "answers_available": [
                        {
                            "id": answer_available.pk,
                            "label": answer_available.label,
                            "is_right": answer_available.is_right,
                        }
                        for answer_available in question.answer_set.all()
                    ],
                }
                for question in quiz.questions.all()
            ],
            "answers": [
                {
                    "id": answer["answer_id"],
                    "label": models.Answer.objects.get(id=answer["answer_id"]).label,
                    "question": answer["question_id"],
                    "is_right": models.Answer.objects.get(
                        id=answer["answer_id"]
                    ).is_right,
                }
                for answer in data["answers"]
            ],
        }
        self.assertEquals(response.json(), expected_data)

    def test_delete_returns_204(self):
        category = self.create_fake_category(title="Filmes")
        self.build_questions(category)

        quiz = services.create_quiz(category_id=category.pk, user=self.user_player)

        count = models.Quiz.objects.count()

        self.auth()
        response = self.client.delete(
            f"/api/quizzes/{quiz.pk}/",
        )
        self.assertEquals(response.status_code, 204)

        self.assertTrue(models.Quiz.objects.count() < count)
