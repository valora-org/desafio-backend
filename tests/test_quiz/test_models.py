from django.test import TestCase
from unittest import mock
import pytest


# Tips:
# refresh_from_db() if you delete or update a field from a model instance
# validators are caled with clean methods


class QuizTestCase(TestCase):

    def test_pytest_working(self):
        assert True