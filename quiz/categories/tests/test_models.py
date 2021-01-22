from django.db.utils import IntegrityError

import pytest

from quiz.categories.models import Category

pytestmark = pytest.mark.django_db


def test_category_str(category: Category):
    """Check category string representation."""
    assert str(category) == category.name


def test_unique_name(category: Category):
    """Assert integrity error by name unique constraint violation."""
    with pytest.raises(IntegrityError):
        Category.objects.create(name=category.name)
