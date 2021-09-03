from django.test import TestCase
from .models import Category, Question, Result
from django.contrib.auth import User


class CategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category(category='História')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())


class QuestionModelTest(TestCase):
    def setUp(self):
        self.obj = Category(category='História')
        self.obj.save()
        self.obj = Question(
            category=Category.objects.all().first(),
            question='Q1',
            answer1 = 'A1',
            answer2 = 'A2',
            answer3 = 'A3',
            right_answer = 'A3'
            )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Question.objects.exists())

    def test_create(self):
        self.assertTrue(Answer.objects.exists())


class ResultModelTest(TestCase):
    def setUp(self):
        self.obj = Result(
            user = User.objects.all().first(), # Get current user
            category = Category.objects.all().first(),
            score = 0           # Calculate score after finish quiz
            )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Result.objects.exists())
