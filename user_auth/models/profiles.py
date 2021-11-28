from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import os

USER_TYPE_CHOICES = (
    ('Player', 'Player'),
)


def UploadImage(instance, filename):
    return os.path.join('players', instance.id, str(instance.id), f'{filename}')
 

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Player(CustomUser):
    picture = models.FileField(
        _('foto'), blank=True, default='member-default.jpg', upload_to=UploadImage)

