import re
import pytest
from model_bakery import baker
from rest_framework.test import APITestCase

from quizzes.models import Answer, Question, Ranking


@pytest.mark.django_db
class TestCreateUserView(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        superuser = baker.make(
            "users.User", username="Joao", is_superuser=True)
        player = baker.make("users.User", username="Marcos", is_admin=False)
        self.data = {
            "superuser": superuser,
            "player": player,
        }

    def test_user_creation(self):
        data = {"username": "username", "password": "password"}

        # Test anyone can create a player account
        response = self.client.post(
            "/api/create-user/", data=data, format="json"
        )

        assert response.status_code == 201
        assert response.data["username"] == "username"
        assert response.data["is_admin"] == False

        # Test only superusers can create an admin account
        data = {"username": "new username",
                "password": "password", "is_admin": True}
        response = self.client.post(
            "/api/create-user/", data=data, format="json"
        )

        assert response.status_code == 403

        self.client.force_authenticate(user=self.data["player"])
        response = self.client.post(
            "/api/create-user/", data=data, format="json"
        )
        assert response.status_code == 403

        self.client.force_authenticate(user=self.data["superuser"])
        response = self.client.post(
            "/api/create-user/", data=data, format="json"
        )

        assert response.status_code == 201
        assert response.data["username"] == "new username"
        assert response.data["is_admin"] == True


@pytest.mark.django_db
class TestGetTokenView(APITestCase):
    def test_return_token(self):
        data = {"username": "username", "password": "password"}
        response = self.client.post(
            "/api/create-user/", data=data, format="json"
        )

        # Test get token endpoint return token
        response = self.client.post(
            "/api/token/", data=data, format="json"
        )

        assert response.status_code == 200
        assert "access" in response.data
        assert type(response.data["access"]) is str
