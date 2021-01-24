import pytest

from rest_framework.exceptions import ValidationError

from quiz.questions.serializers import QuestionSerializer

pytestmark = pytest.mark.django_db


def test_serialize_choice_object_to_dict(question):
    """Assert choice object is serialized to dictionary."""
    serializer = QuestionSerializer(instance=question)
    required_fields = {
        'id', 'categories', 'statement', 'choices', 'correct_choice_index'
    }
    assert required_fields == set(serializer.data)


def test_create_question_object(question_payload):
    """Assert question object created from dictionary."""
    serializer = QuestionSerializer(data=question_payload)
    serializer.is_valid(raise_exception=True)
    question = serializer.save()
    assert question.id


@pytest.mark.parametrize('attr, value', [
    ('statement', None),
    ('statement', ''),
    ('categories', None),
    ('categories', []),
    ('categories', [0]),
    ('choices', ['abc', 'abc']),
    ('choices', ['abc', 'abc', '']),
    ('choices', ['abc', 'abc', 'abc', 'abc']),
    ('correct_choice_index', None),
    ('correct_choice_index', -1),
    ('correct_choice_index', 3),
])
def test_create_raises_validation_error(question_payload, attr, value):
    """Assert validation error if 'attr' has 'value'."""
    question_payload[attr] = value
    serializer = QuestionSerializer(data=question_payload)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
