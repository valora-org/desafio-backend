from django.db.utils import IntegrityError

import pytest

from quiz.users.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('attr', ['name', 'username', 'role'])
def test_user_has_attributes(user: User, attr):
    """Assert user object has these attributes."""
    assert attr in user.__dict__


def test_user_str(user: User):
    """Check user string representation."""
    assert str(user) == user.username


def test_unique_username(user: User):
    """Assert integrity error by username unique constraint violation."""
    with pytest.raises(IntegrityError):
        User.objects.create(username=user.username, password=user.username)
