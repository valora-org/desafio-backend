import pytest

from quiz.categories.serializers import CategorySerializer

pytestmark = pytest.mark.django_db


def test_create_category(category_payload):
    """Assert serializer creates a category object."""
    serializer = CategorySerializer(data=category_payload)
    serializer.is_valid(raise_exception=True)
    category = serializer.save()
    assert category.id


def test_serialize_product_to_dictionary(category):
    """Assert category object is properly serialized."""
    serializer = CategorySerializer(instance=category)
    required_fields = {'id', 'name', 'questions_count'}
    assert set(serializer.data) == required_fields
