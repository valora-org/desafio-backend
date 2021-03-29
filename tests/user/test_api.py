import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_user_player_api_register(admin_client):
    user_object = {
        "email": "user@example.com",
        "password": "test_pass",
    }
    url = reverse('api-user:register_player')
    response = admin_client.post(url, data=user_object)

    assert response.status_code == status.HTTP_201_CREATED


def test_user_admin_api_register(admin_client):
    user_object = {
        "email": "user@example.com",
        "password": "test_pass",
    }
    url = reverse('api-user:register_admin')
    response = admin_client.post(url, data=user_object)

    assert response.status_code == status.HTTP_201_CREATED


def test_user_api_list(admin_client):
    url = reverse('api-user:list_user')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK


def test_category_ranking_api(admin_client, category):
    url = reverse('api-user:category_ranking', args=[category.id])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_global_ranking_api(admin_client):
    url = reverse('api-user:global_ranking')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK


def test_user_api_detail(admin_client, user):
    url = reverse('api-user:retrieve_user', args=[user.id])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['id'] == user.id


def test_user_api_put(admin_client, user):
    url = reverse('api-user:update_user', args=[user.id])
    response = admin_client.patch(url, data={
        "email": "new_user@example.com"
    })
    assert response.status_code == status.HTTP_200_OK


def test_user_api_delete(admin_client, user):
    url = reverse('api-user:delete_user', args=[user.id])
    response = admin_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_user_api_authenticate(admin_client, user):
    user_object = {
        "username": user.username,
        "password": user.password
    }

    url = reverse('api-user:authenticate_user')
    response = admin_client.post(url, data=user_object)
    assert response.status_code == status.HTTP_200_OK


