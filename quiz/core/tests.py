from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from quiz.core.models import Category, Question
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category(category='C1')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())


class QuestionModelTest(TestCase):
    def setUp(self):
        self.obj = Category(category='C1')
        self.obj.save()
        self.obj = Question(
            category = Category.objects.all().first(),
            question ='Q1',
            answer1 = 'A1',
            answer2 = 'A2',
            answer3 = 'A3',
            right_answer = 'A1'
            )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Question.objects.exists())


class CategoryApiTest(APITestCase):
    def setUp(self):
        self.url = '/category/'
        self.data = {'category':'C1'}
        self.user_admin = User.objects.create_user('admin', '1', is_staff=True, is_superuser=True)
        self.client.force_authenticate(self.user_admin)
        self.client.post(self.url, self.data, format='json')

    def test_authentication(self):
        self.user_player = User.objects.create_user('player', '1')
        self.client.force_authenticate(self.user_player)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.post(self.url, {'category':'C2'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(id=2).category, 'C2')

    def test_list(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)

    def test_details(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'category': 'C1'})

    def test_update(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.put(f'{self.url}1/', {'category': 'C2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(pk=1).category, 'C2')

    def test_delete(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


class QuestionApiTest(APITestCase):
    def data(self, question):
        return {
            'id': 1, 
            'category': 'http://testserver/category/1/',
            'question':'Q1',
            'answer1':'A1',
            'answer2':'A2',
            'answer3':'A3',
            'right_answer':'A1'
        }
    def setUp(self):
        self.obj = Category(category='C1')
        self.obj.save()
        self.url = '/question/'
        self.data = {
            'category': 'http://127.0.0.1:8000/category/1/',
            'question':'Q1',
            'answer1':'A1',
            'answer2':'A2',
            'answer3':'A3',
            'right_answer':'A1'
            }
        self.user_admin = User.objects.create_user('admin', '1', is_staff=True, is_superuser=True)
        self.client.force_authenticate(self.user_admin)
        self.client.post(self.url, self.data, format='json')

    def test_create(self):
        data2 = {
            'category': 'http://127.0.0.1:8000/category/1/',
            'question':'Q2',
            'answer1':'A1',
            'answer2':'A2',
            'answer3':'A3',
            'right_answer':'A1'
            }
        self.client.force_authenticate(self.user_admin)
        response = self.client.post(self.url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Question.objects.get(id=2).question, 'Q2')

    def test_list(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.count(), 1)

    def test_details(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1, 
            'category': 'http://testserver/category/1/',
            'question':'Q1',
            'answer1':'A1',
            'answer2':'A2',
            'answer3':'A3',
            'right_answer':'A1'
        })

    def test_update(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.put(f'{self.url}1/', {
            'id': 1, 
            'category': 'http://testserver/category/1/',
            'question':'Q2',
            'answer1':'A1',
            'answer2':'A2',
            'answer3':'A3',
            'right_answer':'A1'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.get(pk=1).question, 'Q2')

    def test_delete(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)


class ChooseQuizApiTest(APITestCase):
    def categories(self):
        for n in range(3):
            self.obj = Category(category=f'C{n+1}')
            self.obj.save()
        return Category.objects.all()

    def create_questions(self):
        for category in self.categories():
            for n in range(10):
                self.obj = Question(
                    category = category,
                    question =f'Q{n+1}',
                    answer1 = 'A1',
                    answer2 = 'A2',
                    answer3 = 'A3',
                    right_answer = 'A1'
                    )
                self.obj.save()
        return Question.objects.all()

    def setUp(self):
        self.create_questions()
        self.url = '/choosequiz/'
        self.user_admin = User.objects.create_user('admin', '1', is_staff=True, is_superuser=True)

    def test_list(self):
        self.client.force_authenticate(self.user_admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(Question.objects.count(), 30)
