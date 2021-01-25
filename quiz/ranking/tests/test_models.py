import pytest

from quiz.ranking.models import CategoryScore, Profile

pytestmark = pytest.mark.django_db


def test_profile_str(profile: Profile):
    """Check profile string representation."""
    assert str(profile)


def test_profile_general_score(profile: Profile):
    """Check profile general score sum."""
    cat_score_1 = profile.category_scores.all().first().score
    cat_score_2 = profile.category_scores.all().last().score
    assert profile.general_score == cat_score_1 + cat_score_2


def test_category_score_str(category_score: CategoryScore):
    """Check category score string representation."""
    assert str(category_score)
