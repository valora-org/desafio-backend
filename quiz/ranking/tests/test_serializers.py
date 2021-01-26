import pytest

from quiz.ranking.serializers import CategoryScoreSerializer, ProfileSerializer

pytestmark = pytest.mark.django_db


def test_serialize_profile_to_dictionary(profile):
    """Assert category object is properly serialized."""
    serializer = ProfileSerializer(instance=profile)
    required_fields = {'username', 'name', 'general_score'}
    assert set(serializer.data) == required_fields


def test_serialize_category_score_to_dictionary(category_score):
    """Assert category object is properly serialized."""
    serializer = CategoryScoreSerializer(instance=category_score)
    required_fields = {'score', 'username', 'name'}
    assert set(serializer.data) == required_fields
