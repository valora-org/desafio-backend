import re

from django.core import validators
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ]
    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False, blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


class Category(models.Model):
    description = models.TextField(unique=True)

    REQUIRED_FIELDS = ['description']

    def __str__(self):
        return self.description


class Answer(models.Model):
    answer = models.TextField()
    is_right = models.BooleanField()

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.TextField()
    answer = models.ManyToManyField(Answer)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.question


class Quiz(models.Model):
    questions = models.ManyToManyField(Question, name='questions')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    correct_answers = models.IntegerField(blank=True, default=0)
    finish = models.DateTimeField(auto_now=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.pk} - {self.user} - {self.correct_answers}"
