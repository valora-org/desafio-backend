from random import randint
from sys import maxsize

from django.urls import resolve
from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db


def test_categories_list_url():
    """Test categories endpoint url for get and post methods."""
    view_name = 'api-v1:categories-list'
    path = '/api/v1/categories/'
    assert reverse(view_name) == path
    assert resolve(path).view_name == view_name


def test_category_detail_url():
    """Test categories endpoint url for get, put, patch and delete methods."""
    category_id = randint(1, maxsize)
    view_name = 'api-v1:categories-detail'
    path = f'/api/v1/categories/{category_id}/'
    assert reverse(view_name, kwargs={'pk': category_id}) == path
    assert resolve(path).view_name == view_name
