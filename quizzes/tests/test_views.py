from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework.views import status

from categories.models import Category
from quizzes.models import Quiz


class QuizViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker()
        cls.url = reverse('list-create-quiz')

        cls.category_data = {'name': 'Programming'}
        cls.category = Category.objects.create(**cls.category_data)

        [
            Quiz.objects.create(
                **{'name': fake.unique.last_name(), 'category': cls.category}
            )
            for _ in range(3)
        ]

        cls.quiz_data = {'name': 'Banco De Dados', 'category': cls.category.id}

    def test_quiz_creation(self):
        response = self.client.post(self.url, self.quiz_data)

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['name'], self.quiz_data['name'])
        self.assertEqual(response.data['category'], self.quiz_data['category'])
        self.assertIsInstance(response.data['id'], str)

    def test_quiz_creation_fields(self):
        response = self.client.post(self.url, self.quiz_data)
        expected_return_fields = {
            'id',
            'name',
            'created_at',
            'category',
        }

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(len(response.data.keys()), 4)
        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

    def test_list_quizzes(self):
        response = self.client.get(self.url)
        self.assertIs(status.HTTP_200_OK, response.status_code)
        self.assertIsInstance(response.json(), list)


class QuizDetailViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker()
        cls.category_data = {'name': 'Programming'}

        cls.category = Category.objects.create(
            **{'name': fake.unique.last_name()}
        )

        cls.quiz_data = {'name': 'Banco De Dados', 'category': cls.category.id}
        cls.quiz = Quiz.objects.create(
            **{'name': 'Back Enquiz', 'category': cls.category}
        )

    def test_retrieve_quiz(self):
        response = self.client.get(f'/quizzes/{self.quiz.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update_quiz(self):
        response = self.client.patch(
            f'/quizzes/{self.quiz.id}/', {'name': 'Fruits'}
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_quiz(self):
        response = self.client.delete(f'/quizzes/{self.quiz.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_retrieve_quiz_fails_not_found(self):
        fake = Faker()
        response = self.client.get(f'/quizzes/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_update_quiz_fails_not_found(self):
        fake = Faker()
        response = self.client.patch(f'/quizzes/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_delete_quiz_fails_not_found(self):
        fake = Faker()
        response = self.client.delete(f'/quizzes/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})
