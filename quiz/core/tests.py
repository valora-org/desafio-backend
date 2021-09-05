from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from quiz.core.models import Category, Question


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
        self.client.post(self.url, self.data, format='json')

    def test_create(self):
        response = self.client.post(self.url, {'category':'C2'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(id=2).category, 'C2')

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)

    def test_details(self):
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'category': 'C1'})

    def test_update(self):
        response = self.client.put(f'{self.url}1/', {'category': 'C2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(pk=1).category, 'C2')

    def test_delete(self):
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
        response = self.client.post(self.url, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Question.objects.get(id=2).question, 'Q2')

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Question.objects.count(), 1)

    def test_details(self):
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
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)
