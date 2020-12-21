from django.test import TestCase
from ..models import Category, Question, Answer, Classification
from django.contrib.auth.models import User, Group


# ------------------------------------------------------------------------
# To run
# python manage.py test quiz
# ------------------------------------------------------------------------


class CategoryTest(TestCase):
    """ Test for Category model """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Category1')

    def test_category_field_name(self):
        print('test_category_field_name')
        cat = Category.objects.get(id=1)
        field_label = cat._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_name(self):
        print('test_category_name')
        cat = Category.objects.get(id=1)
        self.assertEquals(cat.name, 'Category1')


class QuestionTest(TestCase):
    """ Test for Question model """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cat = Category.objects.create(name='Category')
        Question.objects.create(category=cat, choice_A='A', choice_B='B', choice_C='C', question_text="text",
                                right_choice='A')

    def test_question(self):
        print('test_question')
        question = Question.objects.filter(choice_A='A', choice_B='B', choice_C='C', question_text="text",
                                           right_choice='A').first()
        self.assertEqual(question.choice_A, "A")
        self.assertEqual(question.choice_B, "B")
        self.assertEqual(question.choice_C, "C")
        self.assertEqual(question.question_text, "text")
        self.assertEqual(question.right_choice, "A")


class AnswerTest(TestCase):
    """ Test for Answer model """

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.group = Group.objects.create(name="Player")
        self.user = User.objects.create_user('user', 'user@crazymail.com', 'password')
        self.cat = Category.objects.create(name='Category')
        self.question = Question.objects.create(category=self.cat, choice_A='A', choice_B='B', choice_C='C', question_text="text",
                                                right_choice='A')
        self.answer = Answer.objects.create(category=self.cat, question=self.question, author=self.user, author_answer='A', is_correct=False)

    def test_answer(self):
        print('test_answer')
        self.assertEqual(self.answer.question, self.question)
        self.assertEqual(self.answer.author, self.user)
        self.assertEqual(self.answer.category, self.cat)
        self.assertEqual(self.answer.author_answer, 'A')
        self.assertEqual(self.answer.is_correct, False)

    def tearDown(self):
        self.group.delete()
        self.question.delete()
        self.answer.delete()


class ClassificationTest(TestCase):
    """ Test for Classification model """
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.group = Group.objects.create(name="Player")
        self.user = User.objects.create_user('user', 'user@crazymail.com', 'password')
        self.cat = Category.objects.create(name='Category')
        self.classification = Classification.objects.create(category=self.cat, author=self.user, points=0)

    def test_classification(self):
        print('test_classification')
        self.assertEqual(self.classification.category, self.cat)
        self.assertEqual(self.classification.author, self.user)
        self.assertEqual(self.classification.points, 0)

    def tearDown(self):
        self.group.delete()

