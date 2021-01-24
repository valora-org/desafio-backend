import pytest

from rest_framework import status
from rest_framework.test import force_authenticate

from quiz.questions.views import QuestionViewSet
from quiz.users.models import User

pytestmark = pytest.mark.django_db

# Create


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_201_CREATED),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_create_permissions(rf, question_payload, user, role, expected_status):
    """Test permissions for create."""
    view = QuestionViewSet.as_view({'post': 'create'})
    request = rf.post('/fake-url/', data=question_payload)
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request)
    assert response.status_code == expected_status


# List


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_200_OK),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_list_all_status_code(rf, user, role, expected_status):
    """Test list method should return status code 200."""
    view = QuestionViewSet.as_view({'get': 'list'})
    request = rf.get('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request)
    assert response.status_code == expected_status


# Retrieve


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_200_OK),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_retrieve_status_200(rf, question, user, role, expected_status):
    """Test list method should return status code 200."""
    view = QuestionViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=question.id)
    assert response.status_code == expected_status


# Update


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_200_OK),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_update_permissions(rf, question, question_payload, user, role,
                            expected_status, ct):
    """Test permissions for update."""
    view = QuestionViewSet.as_view({'put': 'update'})
    request = rf.put('/fake-url/', data=question_payload, content_type=ct)
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=question.id)
    assert response.status_code == expected_status


# Partial update


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_200_OK),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_partial_update_permissions(rf, question, question_payload, user, role,
                                    expected_status, ct):
    """Test permissions for partial update."""
    view = QuestionViewSet.as_view({'patch': 'update'})
    request = rf.patch('/fake-url/', data=question_payload, content_type=ct)
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=question.id)
    assert response.status_code == expected_status


# Delete


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_204_NO_CONTENT),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_delete_permissions(rf, question, user, role, expected_status):
    """Test permissions for delete."""
    view = QuestionViewSet.as_view({'delete': 'destroy'})
    request = rf.delete('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=question.id)
    assert response.status_code == expected_status


# Bad request


@pytest.mark.parametrize('attr, value', [
    ('statement', ''),
    ('categories', []),
    ('categories', [0]),
    ('choices', ['abc', 'abc']),
    ('choices', ['abc', 'abc', '']),
    ('choices', ['abc', 'abc', 'abc', 'abc']),
    ('correct_choice_index', -1),
    ('correct_choice_index', 3),
])
def test_create_bad_request(rf, user, question_payload, attr, value):
    """Assert bad request for invalid payload."""
    question_payload[attr] = value
    view = QuestionViewSet.as_view({'post': 'create'})
    request = rf.post('/fake-url/', data=question_payload)
    user.role = User.Role.ADMIN
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
