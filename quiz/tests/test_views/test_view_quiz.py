import random
from user_auth.models.profiles import Player
from quiz.models.quiz import Quiz
from django.test import TestCase
from rest_framework.test import APITestCase
from user_auth.tests.utils import *
from quiz.tests.utils import *

class ProfileUnauthorizedQuizQuestionTest(APITestCase):
 
    #quiz view test
    def test_view_list_quiz(self):
        response = self.client.get('/game/quiz/')
        self.assertEqual(response.status_code, 401)

    def test_view_retrieve_quiz(self):
        response = self.client.get(f'/game/quiz/{id}/')
        self.assertEqual(response.status_code, 401)

    #questions view test
    def test_view_list_question_by_category(self):
        id = QuizFactory().id
        response = self.client.get(f'/game/quiz/{id}/questions/')
        self.assertEqual(response.status_code, 401)


    #rank  view test

    def test_view_rank(self):
        response = self.client.get('/game/rank/')
        self.assertEqual(response.status_code, 401)


class ProfileAuthorizedTest(APITestCase):
    
    def setUp(self):
        super().setUp()
        number_of_authors = 2
        
        for id in range(number_of_authors):
            email = f"{id}@email"
            Player.objects.create_user(
                email=email,username=email, first_name=f'william{id}',password="defaultPass123"
            )
        user_one = Player.objects.all().last()
        
        response = self.client.post("/api/token/",{
            "email":user_one.username,
            "password": "defaultPass123"
        })

        self.assertEqual(response.status_code, 200)
        access = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access)

        self.quiz_one = Quiz.objects.create(category="animais")


    def test_view_list_quizzes(self):
        response = self.client.get('/game/quiz/')
        self.assertEqual(response.status_code, 200)

    def test_view_retrieve_quiz(self):
        id = self.quiz_one.id
        response = self.client.get(f'/game/quiz/{id}/')
        self.assertEqual(response.status_code, 200)

    