from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account
from categories.models import Category


class CategoryViewTest(APITestCase):
    def setUp(self) -> None:
        fake = Faker()
        self.url = reverse('list-create-category')

        self.superuser_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': True,
            'password': fake.password(),
        }

        self.category_data = {'name': 'Programming'}

        [
            Category.objects.create(**{'name': fake.unique.last_name()})
            for _ in range(3)
        ]

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_category_creation(self):
        response = self.client.post(self.url, self.category_data)

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['name'], self.category_data['name'])
        self.assertIsInstance(response.data['id'], str)

    def test_category_creation_fields(self):
        response = self.client.post(self.url, self.category_data)
        expected_return_fields = {
            'id',
            'name',
        }

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(len(response.data.keys()), 2)
        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

    def test_list_categories(self):
        response = self.client.get(self.url)
        self.assertIs(status.HTTP_200_OK, response.status_code)
        self.assertIsInstance(response.json(), list)


class CategoryDetailViewTest(APITestCase):
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

        superuser: Account = Account.objects.create(**self.superuser_data)
        self.token = Token.objects.create(user=superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_retrieve_category(self):
        response = self.client.get(f'/categories/{self.category.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_update_category(self):
        response = self.client.patch(
            f'/categories/{self.category.id}/', {'name': 'Foods'}
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_category(self):
        response = self.client.delete(f'/categories/{self.category.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_retrieve_category_fails_not_found(self):
        fake = Faker()
        response = self.client.get(f'/categories/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_update_category_fails_not_found(self):
        fake = Faker()
        response = self.client.patch(f'/categories/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_delete_category_fails_not_found(self):
        fake = Faker()
        response = self.client.delete(f'/categories/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})
