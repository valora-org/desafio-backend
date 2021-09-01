from django.test import TestCase
from .models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category(category='História')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())
