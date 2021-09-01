from django.test import TestCase
from .models import Category, Question


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
        self.assertTrue(Category.objects.exists())
