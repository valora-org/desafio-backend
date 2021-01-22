import pytest

from rest_framework import status
from rest_framework.test import force_authenticate

from quiz.categories.views import CategoryViewSet
from quiz.users.models import User

pytestmark = pytest.mark.django_db

# Create


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_201_CREATED),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_create_permissions(rf, category_payload, user, role, expected_status):
    """Test permissions for create."""
    view = CategoryViewSet.as_view({'post': 'create'})
    request = rf.post('/fake-url/', data=category_payload)
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request)
    assert response.status_code == expected_status


# List


@pytest.mark.parametrize('role', [User.Role.ADMIN, User.Role.PLAYER])
def test_list_all_status_200(rf, user, role):
    """Test list method should return status code 200."""
    view = CategoryViewSet.as_view({'get': 'list'})
    request = rf.get('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request)
    assert response.status_code == status.HTTP_200_OK


# Retrieve


@pytest.mark.parametrize('role', [User.Role.ADMIN, User.Role.PLAYER])
def test_retrieve_status_200(rf, category, user, role):
    """Test list method should return status code 200."""
    view = CategoryViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=category.id)
    assert response.status_code == status.HTTP_200_OK


# Update


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_200_OK),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_update_permissions(rf, category, category_payload, user, role,
                            expected_status, ct):
    """Test permissions for update."""
    view = CategoryViewSet.as_view({'put': 'update'})
    request = rf.put('/fake-url/', data=category_payload, content_type=ct)
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=category.id)
    assert response.status_code == expected_status


# Partial update


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_200_OK),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_partial_update_permissions(rf, category, category_payload, user, role,
                                    expected_status, ct):
    """Test permissions for partial update."""
    view = CategoryViewSet.as_view({'patch': 'update'})
    request = rf.patch('/fake-url/', data=category_payload, content_type=ct)
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=category.id)
    assert response.status_code == expected_status


# Delete


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_204_NO_CONTENT),
                          (User.Role.PLAYER, status.HTTP_403_FORBIDDEN)])
def test_delete_permissions(rf, category, user, role, expected_status):
    """Test permissions for delete."""
    view = CategoryViewSet.as_view({'delete': 'destroy'})
    request = rf.delete('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, pk=category.id)
    assert response.status_code == expected_status
