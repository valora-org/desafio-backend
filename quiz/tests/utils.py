import factory
from quiz.models.quiz import *
from PIL import Image
from  io import BytesIO

from io import StringIO
# in python 3: from io import StringIO
from django.core.files.base import File

#Mock custom user
class QuizFactory(factory.Factory):
    class Meta:
        model = Quiz



def get_image(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)