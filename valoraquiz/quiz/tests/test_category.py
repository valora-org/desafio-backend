import uuid

from quiz import models

from . import base


class CategoryBaseTest(base.RestBaseTest):
    def setUp(self):
        super().setUp()
        self.payload = {
            "title": f"Category {uuid.uuid4()}",
        }


class CategoryTest(CategoryBaseTest):
    def test_create_returns_201(self):

        self.assertEquals(models.Category.objects.count(), 1)

        self.auth(is_admin=True)
        response = self.client.post("/api/categories/", self.payload)
        self.assertEquals(response.status_code, 201)

        self.assertEquals(models.Category.objects.count(), 2)

        category = models.Category.objects.last()
        expected_data = {
            "id": category.pk,
            "title": self.payload["title"],
        }
        self.assertEquals(response.json(), expected_data)

    def test_detail_returns_200(self):
        category = self.create_fake_category(title="Category1")

        self.auth(is_admin=True)
        response = self.client.get(f"/api/categories/{category.pk}/")
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": category.pk,
            "title": category.title,
        }
        self.assertEquals(response.json(), expected_data)

    def test_list_returns_200(self):

        self.auth(is_admin=True)
        response = self.client.get(f"/api/categories/")
        self.assertEquals(response.status_code, 200)

        expected_data = [
            {
                "id": self.fake_category.pk,
                "title": self.fake_category.title,
            }
        ]
        self.assertEquals(response.json(), expected_data)

    def test_complete_update_returns_200(self):
        category = self.create_fake_category(title="Category1")

        payload = {
            "title": "Category2",
        }

        self.auth(is_admin=True)
        response = self.client.put(
            f"/api/categories/{category.pk}/", payload, format="json"
        )
        self.assertEquals(response.status_code, 200)

        expected_data = {
            "id": category.pk,
            "title": payload["title"],
        }
        self.assertEquals(response.json(), expected_data)

    def test_delete_returns_204(self):
        category = self.create_fake_category(title="Category1")

        self.auth(is_admin=True)
        response = self.client.delete(f"/api/categories/{category.pk}/")
        self.assertEquals(response.status_code, 204)
