from django.contrib.auth import get_user_model

import pytest

from rest_framework.exceptions import AuthenticationFailed, ValidationError

from quiz.users.serializers import LoginSerializer
from quiz.users.serializers import SignupSerializer

pytestmark = pytest.mark.django_db

User = get_user_model()

# Signup


def test_creates_user_by_data(user_payload):
    """Test a user is correctly created up to dictionary data."""
    serializer = SignupSerializer(data=user_payload)
    assert serializer.is_valid()
    user = serializer.save()
    assert type(user) is User
    assert user.username == user_payload['username']
    assert user.name == user_payload['name']
    assert user.password != user_payload['password']


@pytest.mark.parametrize('attr', ['username', 'password', 'role'])
def test_creates_missing_required_attribute(user_payload, attr):
    """Test if data with no password is invalid."""
    del user_payload[attr]
    serializer = SignupSerializer(data=user_payload)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


# Login


def test_login_existing_user(user_credentials):
    """Test an existing user may login and get access tokens."""
    serializer = LoginSerializer(data=user_credentials)
    serializer.is_valid(raise_exception=True)
    tokens = serializer.validated_data
    assert tokens.keys() == {'access', 'refresh'}


def test_login_invalid_credentials(user_payload):
    """Test authentication failed for invalid credentials."""
    serializer = LoginSerializer(data=user_payload)
    with pytest.raises(AuthenticationFailed):
        serializer.is_valid(raise_exception=True)
