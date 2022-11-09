from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account
from categories.models import Category
from questions.models import Question
from quizzes.models import Quiz


class QuestionViewTest(APITestCase):
    def setUp(self) -> None:
        fake = Faker('pt_BR')
        self.url = reverse('list-create-question')

        self.superuser_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': True,
            'password': fake.password(),
        }

        self.category_data = {'name': fake.name()}
        self.category = Category.objects.create(**self.category_data)

        self.quiz_data = {'name': fake.sentence(), 'category': self.category}
        self.quiz = Quiz.objects.create(**self.quiz_data)

        self.question_data = {
            'question': fake.sentence(),
            'level': 'Difícil',
            'is_active': True,
            'quiz': self.quiz.id,
        }

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_question_creation(self):
        response = self.client.post(self.url, self.question_data)

        self.assertIs(status.HTTP_201_CREATED, response.status_code)

    def test_question_creation_fields(self):
        response = self.client.post(self.url, self.question_data)
        expected_return_fields = {
            'id',
            'question',
            'level',
            'created_at',
            'is_active',
            'quiz',
        }

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(len(response.data.keys()), 6)
        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

    def test_list_questions(self):
        fake = Faker()
        question = {
            'question': fake.sentence(),
            'level': 'Muito Difícil',
            'is_active': fake.boolean(chance_of_getting_true=25),
            'quiz': self.quiz,
        }
        [Question.objects.create(**question) for _ in range(3)]

        response = self.client.get(self.url)

        self.assertIs(status.HTTP_200_OK, response.status_code)
        self.assertIsInstance(response.json(), list)


class QuestionDetailViewTest(APITestCase):
    def setUp(self) -> None:
        fake = Faker('pt_BR')

        self.superuser_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': True,
            'password': fake.password(),
        }

        self.category_data = {'name': fake.name()}
        self.category = Category.objects.create(**self.category_data)

        self.quiz_data = {'name': fake.sentence(), 'category': self.category}
        self.quiz = Quiz.objects.create(**self.quiz_data)

        self.question_data = {
            'question': fake.sentence(),
            'level': 'Difícil',
            'is_active': True,
            'quiz': self.quiz,
        }
        self.question = Question.objects.create(**self.question_data)

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_retrieve_question(self):
        response = self.client.get(f'/questions/{self.question.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update_question(self):
        fake = Faker()
        response = self.client.patch(
            f'/questions/{self.question.id}/', {'question': fake.sentence()}
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_question(self):
        response = self.client.delete(f'/questions/{self.question.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_retrieve_question_fails_not_found(self):
        fake = Faker()
        response = self.client.get(f'/questions/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_update_question_fails_not_found(self):
        fake = Faker()
        response = self.client.patch(f'/questions/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_delete_question_fails_not_found(self):
        fake = Faker()
        response = self.client.delete(f'/questions/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})
