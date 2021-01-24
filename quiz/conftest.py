from typing import Dict

import pytest

from quiz.categories.models import Category
from quiz.categories.tests.factories import CategoryFactory
from quiz.questions.models import Question
from quiz.questions.tests.facories import QuestionFactory
from quiz.users.models import User
from quiz.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """Media storage for tests."""
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    """User instance for tests."""
    return UserFactory()


@pytest.fixture
def user_payload() -> Dict[str, str]:
    """User payload for signup."""
    return UserFactory.as_dict()


@pytest.fixture
def user_credentials() -> Dict[str, str]:
    """Create a user and return its credentials."""
    user_data = UserFactory.as_dict()
    user = User.objects.create_user(**user_data)
    user.save()
    return {
        'username': user_data['username'],
        'password': user_data['password'],
    }


@pytest.fixture
def ct() -> str:
    """Return content type."""
    return 'application/json; charset=utf-8'


@pytest.fixture
def category() -> Category:
    """Category instance."""
    return CategoryFactory()


@pytest.fixture
def category_payload() -> Dict[str, str]:
    """Category payload."""
    return CategoryFactory.as_dict()


@pytest.fixture
def question() -> Question:
    """Question instance."""
    return QuestionFactory()


@pytest.fixture
def question_payload() -> Dict:
    """Question payload."""
    return QuestionFactory.as_dict()
