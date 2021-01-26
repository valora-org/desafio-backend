import pytest

from rest_framework import status
from rest_framework.test import force_authenticate

from quiz.ranking.views import RankingViewSet
from quiz.users.models import User

pytestmark = pytest.mark.django_db

# List


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_403_FORBIDDEN),
                          (User.Role.PLAYER, status.HTTP_200_OK)])
def test_list_all_status_code(rf, user, role, expected_status):
    """Assert permission for player only."""
    view = RankingViewSet.as_view({'get': 'list'})
    request = rf.get('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request)
    assert response.status_code == expected_status


@pytest.mark.parametrize('role, expected_status',
                         [(User.Role.ADMIN, status.HTTP_403_FORBIDDEN),
                          (User.Role.PLAYER, status.HTTP_200_OK)])
def test_retrieve_status_code(rf, category_score, user, role, expected_status):
    """Assert permission for player only."""
    view = RankingViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    user.role = role
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, category_id=category_score.category.id)
    assert response.status_code == expected_status


def test_retrieve_status_404(rf, user):
    """Asser not foud for a not existing category id."""
    view = RankingViewSet.as_view({'get': 'retrieve'})
    request = rf.get('/fake-url/')
    user.role = User.Role.PLAYER
    request.user = user
    force_authenticate(request, user=request.user)
    response = view(request, category_id=0)
    assert response.status_code == status.HTTP_404_NOT_FOUND
