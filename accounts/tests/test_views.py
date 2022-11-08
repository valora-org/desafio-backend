from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework.views import status

from accounts.models import Account


class AccountViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker('en_UK')
        cls.url = reverse('list-create-account')
        cls.account_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': False,
            'username': fake.user_name(),
            'password': fake.password(),
        }

        [
            Account.objects.create_user(
                **{
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'email': fake.unique.email(),
                    'is_superuser': False,
                    'username': fake.user_name(),
                    'password': fake.password(),
                }
            )
            for _ in range(3)
        ]

    def test_user_signup(self):
        response = self.client.post(self.url, self.account_data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_signup_account_fields(self):
        response = self.client.post(self.url, self.account_data)
        expected_return_fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'date_joined',
            'is_superuser',
        )

        self.assertIs(status.HTTP_201_CREATED, response.status_code)
        self.assertNotIn('password', response.json())
        self.assertEqual(len(response.data.keys()), 8)
        for expected_field in expected_return_fields:
            self.assertIn(expected_field, response.data)

    def test_list_accounts(self):
        response = self.client.get(self.url)

        self.assertIs(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 3)


class AccountDetailViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker()
        cls.account_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'is_superuser': False,
            'username': fake.user_name(),
            'password': fake.password(),
        }

        cls.account: Account = Account.objects.create_user(**cls.account_data)

    def test_retrieve_account(self):
        response = self.client.get(f'/accounts/{self.account.id}/')

        self.assertIs(status.HTTP_200_OK, response.status_code)

    def test_update_account(self):
        response = self.client.patch(
            f'/accounts/{self.account.id}/', {'username': 'austenkate'}
        )

        self.assertIs(status.HTTP_200_OK, response.status_code)

    def test_delete_account(self):
        response = self.client.delete(f'/accounts/{self.account.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_retrieve_account_fails_not_found(self):
        fake = Faker()
        response = self.client.get(f'/accounts/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_update_account_fails_not_found(self):
        fake = Faker()
        response = self.client.patch(f'/accounts/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})

    def test_delete_account_fails_not_found(self):
        fake = Faker()
        response = self.client.delete(f'/accounts/{fake.uuid4()}/')

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertDictEqual(response.json(), {'detail': 'Not found.'})


class SignInViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker('pt_BR')
        cls.url = reverse('signin')
        cls.account_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'username': fake.user_name(),
            'password': fake.password(),
            'is_superuser': False,
        }

        cls.account: Account = Account.objects.create_user(**cls.account_data)
        cls.signin_data = {
            'email': cls.account_data['email'],
            'password': cls.account_data['password'],
        }
        cls.signin_data_without_pass = {'email': cls.account_data['email']}
        cls.signin_data_wrong_pass = {
            'email': cls.account_data['email'],
            'password': 'wrong_password',
        }

    def test_user_signin(self):
        response = self.client.post(self.url, self.signin_data)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_token_field_is_returned(self):
        response = self.client.post(self.url, self.signin_data)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('token', response.data)

    def test_signin_fails_missing_password(self):
        response = self.client.post(self.url, self.signin_data_without_pass)

        self.assertIs(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(
            response.json(), {'password': ['This field is required.']}
        )

    def test_signin_fails_invalid_credentials(self):
        response = self.client.post(self.url, self.signin_data_wrong_pass)

        self.assertIs(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertDictEqual(
            response.json(), {'detail': 'invalid credentials'}
        )
