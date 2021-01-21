from django.urls import resolve
from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db


def test_signup_url():
    """Test signup endpoint url."""
    view_name = 'api-v1:auth-signup'
    path = '/api/v1/auth/signup/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_login_url():
    """Test login endpoint url."""
    view_name = 'api-v1:auth-login'
    path = '/api/v1/auth/login/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name
