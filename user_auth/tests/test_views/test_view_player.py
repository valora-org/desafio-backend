import random
from user_auth.models.profiles import Player
from django.test import TestCase
from rest_framework.test import APITestCase
from user_auth.tests.utils import *

class ProfileUnauthorizedTest(APITestCase):
 
    def test_view_list_player(self):
        response = self.client.get('/profiles/players/')
        self.assertEqual(response.status_code, 401)

    def test_view_retrieve_player(self):
        response = self.client.get(f'/profiles/players/{id}/')
        self.assertEqual(response.status_code, 401)


class ProfileAuthTest(APITestCase):  

    def setUp(self):
        self.user = Player.objects.create(
            email='will@will.com',
            username ='will@will.com',
            password="willPass"
        )

    def test_view_token_400(self):

        response = self.client.post('/api/token/')
        self.assertEqual(response.status_code, 400)
    
    def test_view_token_unauthorized(self):
        data = {
            "password": "not_isValid",
            "email":"pedro@email.com"
        }
        response = self.client.post('/api/token/',data,format='json')
        self.assertEqual(response.status_code, 401)



class ProfileAuthorizedTest(APITestCase):
   

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_authors = 2

        import random

        
        for id in range(number_of_authors):
            email = f"{id}@email"
            Player.objects.create_user(
                email=email,username=email, first_name=f'william{id}',password="defaultPass123"
            )

       
    
    def setUp(self):
        super().setUp()
        user_one = Player.objects.all().last()
        
        response = self.client.post("/api/token/",{
            "email":user_one.username,
            "password": "defaultPass123"
        })

        self.assertEqual(response.status_code, 200)
        access = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access)
        self.access = access



    def test_view_url_exists_at_locator(self):
        response = self.client.get('/profiles/players/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_retrieve_locator(self):
        id = Player.objects.last().id
        response = self.client.get(f'/profiles/players/{id}/')
        self.assertEqual(response.status_code, 200)


    def test_pagination_is_two(self):
        response = self.client.get('/profiles/players/',format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(hasattr(response.content,'count'))
        json_response = response.json()

        self.assertTrue(json_response['count'] == 1)


    def test_create_player(self):
        import json

        player_data = {
            "email": "name@name.com",
            "password":"dfault12pass"
        }

        response = self.client.post(
            "/profiles/players/",
            player_data,
            format='json'
        )
        self.assertEquals(response.status_code, 201)

    def test_patch_lessee(self):

        player_lessee = {            
            "first_name": "marcos",
        }
        player = Player.objects.last()
        response = self.client.patch(f"/profiles/players/{player.id}/", player_lessee, format="json")
        self.assertEquals(response.status_code, 403)
