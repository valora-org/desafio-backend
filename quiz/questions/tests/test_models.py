import pytest

from quiz.questions.models import Question

pytestmark = pytest.mark.django_db


def test_category_str(question: Question):
    """Check question string representation."""
    assert str(question) in question.statement
