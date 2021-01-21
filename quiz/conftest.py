import pytest

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
