from user_auth.models.profiles import Player
from django.test import TestCase


class PlayerTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        email = 'test@test.com'
        Player.objects.create(
            email=email, first_name='william',
        )

    def test_user_type(self):
        player = Player.objects.get(id=1)
        user_type = player.user_type
        self.assertEquals(user_type, 'Player')

