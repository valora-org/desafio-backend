from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from quiz.models import Quiz, Category
from accounts.models import CustomUser as User
# Create your tests here.
class QuizTestCase(APITestCase):
    """
    Test case for quiz app
    """
    def setUp(self) :
        Category.objects.create(name="test")
        Quiz.objects.create(name='Quiz Test', category= Category.objects.first())
        Quiz.objects.create(name='Quiz Test2', category=Category.objects.first())
        Quiz.objects.create(name='Quiz Test3', category=Category.objects.first())
        Quiz.objects.create(name='Quiz Test4', category=Category.objects.first())
        Quiz.objects.create(name='Quiz Test5', category=Category.objects.first())
        Quiz.objects.create(name='Quiz Test6', category=Category.objects.first())
        self.quizzes = Quiz.objects.all()
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser1',
            email= 'testuser@test.com',
            first_name='test', 
            last_name='testuser',
        )
        self.client.login(username='testuser', password='testuser1')

    def test_get_all_quizes(self):
        """
        Test QuizView to get all quizes
        """
        self.assertEqual(self.quizzes.count(), 6)
        response = self.client.get('/api/quizzes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quiz_without_staff_permission(self):
        data = {"name":"QuizTeste", "category":1}
        response = self.client.post(f'/api/quizzes/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_quiz_without_login(self):
        self.client.logout()
        data = {"name":"Test Case","category":1}
        response = self.client.post(f'/api/quizzes/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_quiz_question(self):
        """
        Test to return quiz random question with answers (QuizView)
        """
        self.quizzes = Quiz.objects.first()
        quiz = self.quizzes
        response = self.client.get(f'/api/quizzes/{quiz.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    