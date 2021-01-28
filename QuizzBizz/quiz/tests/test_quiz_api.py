import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from knox.models import AuthToken
from accounts.models import User
from quiz import models as qz

@pytest.mark.django_db

def test_list_quizzes_unauthorized_request():
   
		#Function to test view of listing all quizzes without user authentication
	
   # APICliente instance
   api_client = APIClient()
   # Response
   response = api_client.get('/api/quizzes/')
   # Assert
   assert response.status_code == 401

@pytest.mark.django_db
def test_list_quizzes_authorized_request():
   
		#Function to test view of listing all quizzes with user authentication
	
   # APICliente instance
   api_client = APIClient()
   # Get or Create user
   user, accept = User.objects.get_or_create(username="deilson")
   # Create token
   token = AuthToken.objects.create(user)[1]
   # Insert token in instance APICliente
   api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)
   # Response
   response = api_client.get('/api/quizzes/')
   # Assert
   assert response.status_code == 200

@pytest.mark.django_db
def test_player_quiz_list_unauthorized_request():
   
		#Function to test view of listing all quizzes 
        #answered by the player without user authentication
	
   # APICliente instance
   api_client = APIClient()
   # Response 
   response = api_client.get('/api/my-quizzes/')
   # Assert
   assert response.status_code == 401

@pytest.mark.django_db
def test_player_quiz_list_authorized_request():

		#Function to test view of listing all quizzes 
        #answered by the player with user authentication

   # APICliente instance
   api_client = APIClient()
   # Get or Create user
   user, accept = User.objects.get_or_create(username="tester")
   # Create token
   token = AuthToken.objects.create(user)[1]
   # Insert token in instance APICliente
   api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)
   # Response 
   response = api_client.get('/api/my-quizzes/')
   # Assert
   assert response.status_code == 200

@pytest.mark.django_db
def test_get_quiz_unauthorized_request():
   
		#Function to test view of listing all questions and answers 
        #of single quiz without user authentication
	   

   # Create object quiz
   quiz = qz.Quiz.objects.create(
      name="Quiz Test",
      
      slug="quiz-test",
   )

   # APICliente instance
   api_client = APIClient()
   # Response 
   response = api_client.get('/api/quizzes/' + str(quiz.slug) + '/')
   # Assert
   assert response.status_code == 401

@pytest.mark.django_db
def test_get_quiz_authorized_request():
   
		#Function to test view of listing all questions and answers 
        #of single quiz with user authentication
	

  
   # Create object quiz
   quiz = qz.Quiz.objects.create(
      name="Quiz Test",
      slug="quiz-test",
   )

   # APICliente instance
   api_client = APIClient()
   # Get or Create user
   user, accept = User.objects.get_or_create(username="tester")
   # Create token 
   token = AuthToken.objects.create(user)[1]
   # Insert token in instance APICliente
   api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)
   # Response 
   response = api_client.get('/quiz/quizzes/' + str(quiz.slug) + '/')
   # Assert
   assert response.status_code == 200

@pytest.mark.django_db
def test_ranking_unauthorized_request():
   
		#Function to test view fo overall ranking
        #without user authentication
	

  
   # Create object quiz
   quiz = qz.Quiz.objects.create(
      name="Quiz Test",
      slug="quiz-test",
   )

   # APICliente instance
   api_client = APIClient()
   # Response 
   response = api_client.get('/quiz/ranking/'+ str(quiz.slug) + '/')
   # Assert
   assert response.status_code == 401

@pytest.mark.django_db
def test_ranking_authorized_request():
       
		#Function to test view fo overall ranking 
        #with user authentication
	

    # Create object quiz
   quiz = qz.Quiz.objects.create(
      name="Quiz Test",
      slug="quiz-test",
   )

   # APICliente instance
   api_client = APIClient()
   # Get or Create user
   user, accept = User.objects.get_or_create(username="tester")
   # Create token 
   token = AuthToken.objects.create(user)[1]
   # Insert token in instance APICliente
   api_client.credentials(HTTP_AUTHORIZATION='Token ' + token)
   # Response 
   response = api_client.get('/quiz/ranking/'+ str(quiz.slug) + '/')
   # Assert
   assert response.status_code == 200