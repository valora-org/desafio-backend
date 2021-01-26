from random import randint
from sys import maxsize

from django.urls import resolve
from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db


def test_ranking_list_url():
    """Test ranking endpoint url for get and post methods."""
    view_name = 'api-v1:ranking-list'
    path = '/api/v1/ranking/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_ranking_detail_url():
    """Test ranking endpoint url for get, put, patch and delete methods."""
    category_id = randint(1, maxsize)
    view_name = 'api-v1:ranking-detail'
    path = f'/api/v1/ranking/{category_id}/'
    assert reverse(view_name, kwargs={'category_id': category_id}) == path
    assert resolve(path).view_name == view_name
