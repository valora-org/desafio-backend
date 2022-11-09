from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User
from categories.models import Category


user = {"email": "user@mail.com", "username": "user", "password": "123"}
admin = {"email": "admin@mail.com", "username": "admin", "password": "123"}


class CategoryViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

    def test_list_all_categories(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/categories/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_categories_not_loggedIn(self):
        response = self.client.get("/api/categories/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_category(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.post("/api/categories/", data={"name": "Category"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"id": 1, "name": "Category"})

    def test_create_category_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.post("/api/categories/", data={"name": "Category"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data,
            {"detail": "You do not have permission to perform this action."},
        )


class CategorySingleViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        User.objects.create_superuser(**admin)
        admin_token = Token.objects.get_or_create(user_id="1")
        self.admin_token = admin_token[0]

        User.objects.create_user(**user)
        user_token = Token.objects.get_or_create(user_id="2")
        self.user_token = user_token[0]

        Category.objects.create(name="Category")

    def test_retrieve_category(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.get("/api/categories/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["category"], {"id": 1, "name": "Category"})

    def test_retrieve_category_not_loggedIn(self):
        response = self.client.get("/api/categories/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_category(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.patch(
            "/api/categories/1/", data={"name": "New Category Name"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["category"], {"id": 1, "name": "New Category Name"}
        )

    def test_patch_category_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.patch(
            "/api/categories/1/", data={"name": "New Category Name"}
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_category(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.admin_token))
        response = self.client.delete("/api/categories/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_category_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.user_token))
        response = self.client.delete("/api/categories/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
