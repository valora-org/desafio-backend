import pytest
from rest_framework.test import APIClient
from accounts.models import User


@pytest.mark.django_db
def test_create_and_login_user_request():
    """
		Function to test view of create and login of user

	"""

    # APICliente instance
    api_client = APIClient()
    
    # Body request
    data = {
        "username": "teste",
        "password": "teste"
    }

    # Response create player
    response_create = api_client.post('/accounts/create/', format='json', data=data)
    # Response login player
    response_login = api_client.post('/accounts/login/', format='json', data=data)

    # Asserts
    assert response_create.status_code == 200
    assert response_login.status_code == 200
