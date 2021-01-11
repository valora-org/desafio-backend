from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from quiz.models import Category, Question

# variáveis globais


username = "usuariotest"
password = "senha123msa"
email = "albertow@gmail.com"
url_category = 'http://127.0.0.1:8000/category/'
url_category_id = 'http://127.0.0.1:8000/category/1/'
url_question = 'http://127.0.0.1:8000/question/'
url_question_id = 'http://127.0.0.1:8000/question/1/'


class CategoryTestCase(APITestCase):
    """ Teste com usuário adm ,
     crud categotia [PUT,POST,GET,DELETE] """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username=username, email=email, password=password)
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def teste_list_category(self):
        self.response = self.client.get(url_category)
        self.assertEquals(self.response.status_code, 200)

    def teste_post_category(self):
        data = {"category": "Python"}
        self.response = self.client.post(url_category, data)
        self.assertEquals(Category.objects.all().count(), 1)
        self.assertEquals(Category.objects.filter(category="Python").count(), 1)

    def teste_put_category(self):
        self.teste_post_category()
        data = {"category": "PythonEditado"}
        self.response = self.client.put(url_category_id, data=data)
        self.assertEquals(self.response.status_code, status.HTTP_200_OK)

    def teste_delete_category(self):
        self.teste_post_category()
        self.response = self.client.delete(url_category_id)
        self.assertEquals(Category.objects.all().count(), 0)
        self.assertEquals(self.response.status_code, status.HTTP_204_NO_CONTENT)


class QuestionTestCase(APITestCase):
    """ Teste com usuário adm ,
     crud questão [PUT,POST,GET,DELETE] """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(username=username, email=email, password=password)
        self.token = Token.objects.create(user=self.user)
        self.client.force_login(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.categoria = Category.objects.create(category="Python")

    def teste_list_question(self):
        self.response = self.client.get(url_question)
        self.assertEquals(self.response.status_code, 200)

    def teste_post_question(self):
        data = {"category": "1", "question": "soma 2 +2 ", "option_a": "2", "option_b": "3", "option_c": "4",
                "correct": "C"}
        self.response = self.client.post(url_question, data, format='json')
        self.assertEquals(Question.objects.all().count(), 1)
        self.assertEquals(Category.objects.filter(category="Python").count(), 1)

    def teste_put_question(self):
        self.teste_post_question()
        data = {"category": "1", "question": "soma 2 +2 ", "option_a": "2", "option_b": "3", "option_c": "4",
                "correct": "A"}
        self.response = self.client.put(url_question_id, data=data, format='json')
        self.assertEquals(Question.objects.first().correct, "A")
        self.assertEquals(self.response.status_code, status.HTTP_200_OK)

    def teste_delete_question(self):
        self.teste_post_question()
        self.assertEquals(Question.objects.all().count(), 1)
        self.response = self.client.delete(url_question_id)
        self.assertEquals(Question.objects.all().count(), 0)
        self.assertEquals(self.response.status_code, status.HTTP_204_NO_CONTENT)


# class QuizTestCase(APITestCase):
#     """ Teste quiz [PUT,POST,GET,DELETE] """
#
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username=username, email=email, password=password)
#         self.token = Token.objects.create(user=self.user)
#         self.client.force_login(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#
#
#     def teste_x_quiz(self):
#         self.response = requests.post('http://127.0.0.1:8000/api-token-auth/', {
#             "username": "admin",
#             "password": "admin123"
#         })
#
#         print(self.response.json()["token"])
#
#         data =  {"question": "soma 2 +2", "correct_user": "C"}
#
#         headers = {
#             'Content-Type': 'application/json',
#             'Accept': 'application/json',
#             'Authorization': 'Token ' + self.response.json()["token"]
#         }
#         self.response = requests.post('http://127.0.0.1:8000/quiz/1/', data=data,
#                                       headers=headers)
#         print(self.response.content)
#         print(UserProfile.objects.all()[0].total_points)
#         self.assertEquals(UserProfile.objects.all()[0].total_points, 1)
