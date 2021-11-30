import factory
from user_auth.models.profiles import CustomUser, Player
from PIL import Image
from django.core.files.images import ImageFile
from  io import BytesIO

from io import StringIO
# in python 3: from io import StringIO
from django.core.files.base import File

#Mock custom user
class UserFactory(factory.Factory):
    class Meta:
        model = CustomUser


#Mock player
class PlayerFactory(factory.Factory):
    class Meta:
        model = Player
    username = "william_user@gmaill.com"
    password = "2pass#123"

#mock image

def get_image(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)