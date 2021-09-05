from rest_framework import test
from rest_framework.authtoken.models import Token

import users.models
import users.choices

from quiz import models


class RestBaseTest(test.APITestCase):
    def setUp(self):
        super().setUp()
        self.user_player = self.create_fake_user(
            username="player",
            password="123",
            email="player@email.com",
            type=users.choices.PLAYER,
        )
        self.user_admin = self.create_fake_user(
            username="admin",
            password="admin123",
            email="admin@email.com",
            type=users.choices.ADMIN,
        )
        self.fake_category = self.create_fake_category("Category1")

    def create_fake_user(
        self,
        username,
        password,
        email,
        type,
    ):
        return users.models.User.objects.create(
            username=username,
            password=password,
            email=email,
            type=type,
        )

    def auth(self, user=None, is_admin=False):
        if not user:
            user = self.user_player

        if is_admin:
            user = self.user_admin

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def create_fake_category(self, title):
        return models.Category.objects.create(title=title)

    def create_fake_question(self, label, category):
        return models.Question.objects.create(label=label, category=category)

    def create_fake_answer(self, label, question, is_right):
        return models.Answer.objects.create(
            label=label, question=question, is_right=is_right
        )
