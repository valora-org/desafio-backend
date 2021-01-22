from django.contrib.auth import get_user_model

import pytest

from rest_framework import status

from quiz.users.views import AuthViewSet

User = get_user_model()

pytestmark = pytest.mark.django_db


def test_signup_status_created(user_payload, rf, ct):
    """Test vaild user payload may sinup with status code 201."""
    view = AuthViewSet.as_view({'post': 'signup'})
    request = rf.post('/fake-url/', data=user_payload, content_type=ct)
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.parametrize('attr', ['password'])
def test_signup_return_has_no_attr(user_payload, rf, ct, attr):
    """Assert succeded signup return data has no given attribute."""
    view = AuthViewSet.as_view({'post': 'signup'})
    request = rf.post('/fake-url/', data=user_payload, content_type=ct)
    response = view(request)
    assert attr not in response.data


@pytest.mark.parametrize('attr', ['username', 'password', 'role'])
def test_signup_missing_attr_return_bad_request(user_payload, rf, ct, attr):
    """Assert signup request with misssing attribute return bad request."""
    view = AuthViewSet.as_view({'post': 'signup'})
    del user_payload[attr]
    request = rf.post('/fake-url/', data=user_payload, content_type=ct)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# Login


def test_login_signedup_ok(user_credentials, rf, ct):
    """Assert existing user is able to login with status ok."""
    view = AuthViewSet.as_view({'post': 'login'})
    request = rf.post('/fake-url/', data=user_credentials, content_type=ct)
    response = view(request)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize('attr', ['access', 'refresh'])
def test_login_return_has_attr(user_credentials, rf, ct, attr):
    """Assert succeded login return data has given attribute."""
    view = AuthViewSet.as_view({'post': 'login'})
    request = rf.post('/fake-url/', data=user_credentials, content_type=ct)
    response = view(request)
    assert attr in response.data


def test_login_non_signedup_unauthorized(user_payload, rf, ct):
    """Assert invalid credentials return status unauthorized."""
    view = AuthViewSet.as_view({'post': 'login'})
    request = rf.post('/fake-url/', data=user_payload, content_type=ct)
    response = view(request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
