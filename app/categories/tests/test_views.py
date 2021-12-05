
import pytest
from model_bakery import baker
from rest_framework.test import APITestCase

from categories.models import Category


@pytest.mark.django_db
class TestCategoryView(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        admin = baker.make("users.User", username="Joao", is_admin=True)
        player = baker.make("users.User", username="Marcos", is_admin=False)
        self.data = {
            "admin": admin,
            "player": player,
        }

    def test_authentication_on_endpoints(self):
        data = {"name": "Sport"}

        # Make request without any user authenticated
        response = self.client.post(
            "/api/category/", data=data, format="json"
        )

        assert response.status_code == 403

        # Make request authenticating with user who has no permission to the endpoint
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.post(
            "/api/category/", data=data, format="json"
        )

        assert response.status_code == 403

        # Make request authenticating with user who has permission to the endpoint
        response = self.client.get(
            "/api/categories/", data=data, format="json"
        )

        assert response.status_code == 200

        # Test admin has permission to create and update category
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.post(
            "/api/category/", data=data, format="json"
        )

        assert response.status_code == 201
        assert Category.objects.count() == 1
        assert Category.objects.last().name == "Sport"

        category = Category.objects.last()

        data = {"name": "Environment"}
        response = self.client.put(
            f"/api/category/{category.id}/", data=data, format="json"
        )

        assert response.status_code == 200
        assert Category.objects.count() == 1
        assert Category.objects.last().name == "Environment"

        # Test player can't update category's name
        data = {"name": "Sport"}
        self.client.force_authenticate(user=self.data["player"])
        response = self.client.put(
            f"/api/category/{category.id}/", data=data, format="json"
        )

        assert response.status_code == 403
        assert Category.objects.last().name == "Environment"

        # Test player can't delete category
        response = self.client.delete(
            f"/api/category/{category.id}/", data=data, format="json"
        )

        assert response.status_code == 403
        assert Category.objects.count() == 1

        # Test admin can delete category
        self.client.force_authenticate(user=self.data["admin"])
        response = self.client.delete(
            f"/api/category/{category.id}/", data=data, format="json"
        )

        assert response.status_code == 204
        assert Category.objects.count() == 0
