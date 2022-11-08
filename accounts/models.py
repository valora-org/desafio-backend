from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

from accounts.managers import CustomAccountManager


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    objects = CustomAccountManager()

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]
    USERNAME_FIELD = 'email'

    categories = models.ManyToManyField(
        to='categories.Category', related_name='accounts'
    )

    def __repr__(self) -> str:
        return '<Account %s - %s>' % (self.id, self.email)
