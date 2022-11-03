from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    categories = models.ManyToManyField(
        to='quizzes.Category', related_name='accounts'
    )
