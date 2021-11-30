from user_auth.models.profiles import CustomUser
from django.test import TestCase


class UserTestClass(TestCase):
    def setUp(self):
        email = 'test@test.com'
        CustomUser.objects.create(
            email=email, first_name='william',
        )

    def test_user_str_(self):
        user = CustomUser.objects.last()
        self.assertEquals(user.__str__(), user.email)


   