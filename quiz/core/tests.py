from django.test import TestCase
from .models import Category, Question, Answer


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
            question='Q1', 
            category=Category.objects.all().first()
            )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Question.objects.exists())


class AnswerModelTest(TestCase):
    def setUp(self):
        self.obj = Category(category='História')
        self.obj.save()
        self.obj = Question(
            question='Q1', 
            category=Category.objects.all().first()
            )
        self.obj.save()
        self.obj = Answer(
            answer = 'A1',
            question=Question.objects.all().first(), 
            category=Category.objects.all().first()
            )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Answer.objects.exists())
