from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Manager for user model."""

    def create_user(self, name, username, role, password=None, **kwargs):
        """Create a new user and set password."""
        if password is None:
            raise TypeError(_('User should set a password'))
        user = self.model(name=name, username=username, role=role, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name='', password=None, **kwargs):
        """Create a new super user."""
        user = self.create_user(name, username, User.Role.SUPERUSER, password,
                                **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    """Default user for Valora Quiz."""

    class Role(models.TextChoices):
        """User role Choices."""
        ADMIN = 'A', _('Admin')
        PLAYER = 'P', _('Player')
        SUPERUSER = 'S', _('Superuser')

    #: First and last name do not cover name patterns around the globe
    name = CharField(_('Name of User'), blank=True, max_length=255)
    username = CharField(_('Username of user'), blank=False, max_length=50,
                         db_index=True, unique=True)
    role = CharField(_('Role of the user'), max_length=1, choices=Role.choices,
                     default=Role.PLAYER)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        """String representation for user instance."""
        return self.username

    class Meta:
        """Meta info for user model."""
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['username']
        indexes = [models.Index(fields=['username'], name='username_idx')]
