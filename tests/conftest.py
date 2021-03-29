from datetime import timedelta
from django.utils import timezone
from oauth2_provider.models import AccessToken, Application
from rest_framework.test import APIClient
from quiz.models import Quiz, Category, Question
from user.models import User, Point
import pytest


@pytest.fixture
def admin_client(admin_user, application_client):
    access_token = AccessToken.objects.create(
        user=admin_user,
        scope="read write",
        expires=timezone.now() + timedelta(seconds=300),
        token="secret-access-token-key",
        application=application_client
    )

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token.token)
    client.force_authenticate(user=admin_user)

    return client


@pytest.fixture
def application_client(admin_user):
    return Application.objects.create(
        name="Test Application",
        redirect_uris="http://localhost http://example.com http://example.org",
        user=admin_user,
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
    )


@pytest.fixture
def question():
    question = Question()
    question.question = "test_question"
    question.answer_A = "A"
    question.answer_B = "B"
    question.answer_C = "C"
    question.save()
    return point


@pytest.fixture
def category():
    category = Category()
    category.name = "teste_category"
    category.save()
    return category


@pytest.fixture
def point():
    point = Point()
    point.category = 1
    point.points = 20
    point.global_point = 40
    point.save()
    return point


@pytest.fixture
def user():
    point = Point()
    point.category = 1
    point.points = 20
    point.global_point = 40
    point.save()

    user = User()
    user.email = "user@example.com"
    user.password = "test_pass"
    user.save()
    user.points.add(point)
    return user


@pytest.fixture
def quiz():
    category = Category()
    category.name = "teste_category"
    category.save()

    question = Question()
    question.question = "test_question"
    question.answer_A = "test_A"
    question.answer_B = "test_B"
    question.answer_C = "test_C"
    question.save()

    quiz = Quiz()
    quiz.title = "test_quiz"
    quiz.category = category
    quiz.save()
    quiz.question.add(question)
    return quiz