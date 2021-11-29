import random
# from users.tests.utils import Base64Handler, EasyTestRefreshToken, RSAhandleTest
from user_auth.models.profiles import Player
from django.test import TestCase
from rest_framework.test import APITestCase

class ProfileUnauthorizedTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_authors = 2

        import random

        
        for id in range(number_of_authors):
            email = f"{id}@email",
            Player.objects.get_or_create(
                email=email,username=email, first_name=f'william{id}',
            )

    def test_view_url_exists_at_Lessee(self):
        response = self.client.get('/players/')
        self.assertEqual(response.status_code, 401)

    def test_view_url_exists_at_retrieve_player(self):
        id = Player.objects.all().first().id
        response = self.client.get(f'/players/{id}/')
        self.assertEqual(response.status_code, 401)



class ProfileDoesNotExistsTest(APITestCase):
   
    def test_view_url_exists_at_retrieve_player(self):
        id = 1
        response = self.client.get(f'/players/{id}/')
        self.assertEqual(response.status_code, 401)


class ProfileAuthTest(APITestCase):
   

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        id = 2

        import random

        
        email = f"{id}@email.com",
        password = f"{id}pass#123"
        Player.objects.get_or_create(
            email=email,username=email,password=password, first_name=f'william{id}',
        )
    

    def test_view_url_400(self):

        response = self.client.post('/api/token/')
        self.assertEqual(response.status_code, 400)

    def test_view_url_200(self):
        user = Player.objects.all().last()
        email = f"{user.id}@email.com",
        password = f"{user.id}pass#123"
        data = {
            'pasword': password,
            'email':email
        }
        response = self.client.post('/api/token/',data,format='json')
        self.assertEqual(response.status_code, 200)


class ProfileAuthorizedTest(APITestCase):
   

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_authors = 2

        import random

        
        for id in range(number_of_authors):
            email = f"{id}@email",
            Player.objects.get_or_create(
                email=email,username=email, first_name=f'william{id}',
            )

       
    
    def setUp(self):
        super().setUp()
        user_one = Player.objects.get(pk=1)
        token  = EasyTestRefreshToken.for_user(str(user_one.unique_id),'profile','lessee')
        access = str(token.access_token)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access)
        self.access = access

        phone = CompleteNumber.objects.create(country_code='55',ddd='61',phone_number=random.randint(11111111,99999999))
        self.user = CustomUser.objects.create(complete_name='name of test',email=f'{id}@test.com',phonenumber=phone)


        #security base
        self.rsa_handler = RSAhandleTest()
        self.base64_handler = Base64Handler()



    def test_view_url_exists_at_locator(self):
        response = self.client.get('/api/v1/lessee/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_retrieve_locator(self):
        id = Player.objects.get(pk=1).id
        response = self.client.get(f'/api/v1/lessee/{id}/')
        self.assertEqual(response.status_code, 200)


    def test_pagination_is_two(self):
        response = self.client.get('/api/v1/lessee/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(hasattr(response.content,'count'))
        json_response = response.json()
        self.assertTrue(json_response['count'] == Player.objects.all().count())


    def test_create_lessee(self):
        import json
        phonenumber = self.user.phonenumber
        data = {"country_code": f"{phonenumber.country_code}", "ddd": f"{phonenumber.ddd}", "phone_number": f"{phonenumber.phone_number}"}

        data = json.dumps(data)
        easy_pass1 = self.rsa_handler.generate_RSA(message=data)

        easy_pass = self.base64_handler.encode_base64(easy_pass1)

        locator_data = {
            "easy_pass": easy_pass,
            "document": "name",
            "document_type":"1"
        }

        response = self.client.post(
            "/api/v1/lessee/",
            locator_data,
            format='json'
        )
        self.assertEquals(response.status_code, 200)


        locator = Player.objects.last()
        locator.refresh_from_db()
        self.locator = locator


    def test_patch_lessee(self):

        update_lessee = {
            
            "name": "marcos",
            "accept_all": True
        }
        lessee = Player.objects.last()
        response = self.client.patch(f"/api/v1/lessee/{lessee.id}/", update_lessee, format="json")

        print(response.content)
        self.assertEquals(response.status_code, 200)
        lessee.refresh_from_db()
