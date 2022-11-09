from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account
from answers.models import Answer
from categories.models import Category
from questions.models import Question
from quizzes.models import Quiz


class AnswerViewTest(APITestCase):
    def setUp(self) -> None:
        fake = Faker('pt_BR')
        self.url = reverse('list-create-answer')

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

        self.answer_data = {
            'answer': fake.sentence(),
            'is_correct': fake.boolean(),
            'question': self.question.id,
        }

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_answer_creation(self):
        response = self.client.post(self.url, self.answer_data)

        self.assertIs(status.HTTP_201_CREATED, response.status_code)

    def test_answer_creation_fields(self):
        response = self.client.post(self.url, self.answer_data)
        expected_return_fields = {
            'id',
            'answer',
            'is_correct',
            'question',
        }

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(len(response.data.keys()), 4)
        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

    def test_list_answers(self):
        fake = Faker()
        answer = {
            'answer': fake.sentence(),
            'is_correct': fake.boolean(chance_of_getting_true=25),
            'question': self.question,
        }
        [Answer.objects.create(**answer) for _ in range(3)]

        response = self.client.get(self.url)

        self.assertIs(status.HTTP_200_OK, response.status_code)
        self.assertIsInstance(response.json(), list)


class AnswerDetailViewTest(APITestCase):
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

        self.answer_data = {
            'answer': fake.sentence(),
            'is_correct': False,
            'question': self.question,
        }

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_retrieve_answer(self):
        fake = Faker()
        answer_data = {
            'answer': fake.sentence(),
            'is_correct': fake.boolean(chance_of_getting_true=25),
            'question': self.question,
        }
        answer: Answer = Answer.objects.create(**answer_data)

        response = self.client.get(f'/answers/{answer.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update_answer(self):
        fake = Faker()
        answer_data = {
            'answer': fake.sentence(),
            'is_correct': fake.boolean(chance_of_getting_true=25),
            'question': self.question,
        }
        answer: Answer = Answer.objects.create(**answer_data)

        response = self.client.patch(
            f'/answers/{answer.id}/', {'answer': fake.sentence()}
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_answer(self):
        fake = Faker()
        answer_data = {
            'answer': fake.sentence(),
            'is_correct': fake.boolean(chance_of_getting_true=25),
            'question': self.question,
        }
        answer: Answer = Answer.objects.create(**answer_data)

        response = self.client.delete(f'/answers/{answer.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_retrieve_answer_fails_not_found(self):
        fake = Faker()
        response = self.client.get(f'/answers/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_update_answer_fails_not_found(self):
        fake = Faker()
        response = self.client.patch(f'/answers/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_delete_answer_fails_not_found(self):
        fake = Faker()
        response = self.client.delete(f'/answers/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})
