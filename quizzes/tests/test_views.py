from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account
from categories.models import Category
from quizzes.models import Quiz


class QuizViewTest(APITestCase):
    def setUp(self) -> None:
        fake = Faker()
        self.url = reverse('list-create-quiz')

        self.superuser_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': True,
            'password': fake.password(),
        }

        self.category_data = {'name': 'Programming'}
        self.category = Category.objects.create(**self.category_data)

        [
            Quiz.objects.create(
                **{'name': fake.unique.last_name(), 'category': self.category}
            )
            for _ in range(3)
        ]

        self.quiz_data = {
            'name': 'Banco De Dados',
            'category': self.category.id,
        }

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

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
    def setUp(self) -> None:
        fake = Faker()

        self.superuser_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': True,
            'password': fake.password(),
        }

        self.category_data = {'name': 'Programming'}

        self.category = Category.objects.create(
            **{'name': fake.unique.last_name()}
        )

        self.quiz_data = {
            'name': 'Banco De Dados',
            'category': self.category.id,
        }
        self.quiz = Quiz.objects.create(
            **{'name': 'Back Enquiz', 'category': self.category}
        )

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

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
