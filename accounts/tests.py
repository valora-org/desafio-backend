from accounts.models import CustomUser as User
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

# Create your tests here.

class UserTestCase(APITestCase):

    def setUp(self):
        
        User.objects.create_user(username= "admintest3", first_name= "admintest3", last_name= "3testadmin",
                                             password= "admintest3123", email= "admin_test3@admin.com")
        User.objects.create_user(username= "admintest4", first_name= "admintest4", last_name= "4testadmin",
                                             password= "admintest4123", email= "admin_test4@admin.com")
        self.testuser = User.objects.first()
        self.user = User.objects.create_user(username= "admintest2", first_name= "admintest2", last_name= "2testadmin",
                                             password= "admintest2123", email= "admin_test2@admin.com")
        self.token = Token.objects.get(user = self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

    def test_create_user(self):
        data = {
            'username': 'admintest', 
            'first_name': 'admintest',
            'last_name': 'testadmin',
            'email':'admintest@admin.com',
            
        }

        response = self.client.post(f'/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_all_user(self):
        response = self.client.get(f'/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    

