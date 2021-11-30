from user_auth.models.profiles import Player
from django.test import TestCase
from user_auth.models import UploadImage
from user_auth.tests.utils import *

class PlayerTestClass(TestCase):
    
    def setUp(self):
        email1 = 'test@test.com'
        email2 = f"1{email1}"

        Player.objects.get_or_create(
            email=email1,username=email1, first_name='william',
        )

        file = get_image()
        Player.objects.get_or_create(
            email=email2,username=email2,first_name='william',picture=file
        )

        self.email1 = email1
        self.email2 = email2

    def test_user_type(self):
        player = Player.objects.get(email=self.email1)
        user_type = player.user_type
        self.assertEquals(user_type, 'Player')


    def test_user_default_picture_path(self):
        player = Player.objects.get(email=self.email1)
        picture = player.picture
        self.assertEquals(str(picture.url), '/media/member-default.jpg' )

    def test_default_picture_upload_to(self):
        player = Player.objects.get(email=self.email2)
        picture = player.picture
        upload_to = str(UploadImage(player,picture.file.name))
        self.assertEquals(f"/code{picture.url}",upload_to)
