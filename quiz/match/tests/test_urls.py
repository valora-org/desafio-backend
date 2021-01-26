from django.urls import resolve
from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db


def test_new_match_url():
    """Test endpoint url for new match."""
    view_name = 'api-v1:match-new'
    path = '/api/v1/match/new/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_open_match_url():
    """Test endpoint url for getting open match."""
    view_name = 'api-v1:match-open'
    path = '/api/v1/match/open/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_match_response_url():
    """Test url for send response for open match."""
    view_name = 'api-v1:match-response'
    path = '/api/v1/match/response/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name
