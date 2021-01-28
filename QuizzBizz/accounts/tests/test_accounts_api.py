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
    response_create = api_client.post(reverse('register-account'), format='json', data=data)