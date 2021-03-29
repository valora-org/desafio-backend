import pytest
from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


def test_quiz_list(admin_client):
    url = reverse('api-quiz:list_quiz')
    response = admin_client.get(url, content_type="application/json")
    assert response.status_code == status.HTTP_200_OK


def test_quiz_api_detail(admin_client, quiz):
    url = reverse('api-quiz:retrieve_quiz', args=[quiz.id])
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['id'] == quiz.id


def test_quiz_api_update(admin_client, quiz):
    url = reverse('api-quiz:update_quiz', args=[quiz.id])
    response = admin_client.patch(url, data={'title': 'new_title'})
    assert response.status_code == status.HTTP_200_OK


def test_quiz_api_delete(admin_client, quiz):
    url = reverse('api-quiz:delete_quiz', args=[quiz.id])
    response = admin_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
