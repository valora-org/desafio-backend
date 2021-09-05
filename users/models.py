from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(email=self.normalize_email(email))

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)
        usuario.save()

        return usuario


class User(AbstractUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True,
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        null=True,
        blank=True,
        help_text=_(
            "150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo", default=True
    )
    is_staff = models.BooleanField(
        verbose_name="Usuário é staff", default=False
    )
    is_superuser = models.BooleanField(
        verbose_name="Usuário é super usuário", default=False
    )
    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "user"

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        "users.User",
        verbose_name="User Profile",
        on_delete=models.DO_NOTHING,
    )
    score = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        db_table = "profile"

    def __str__(self) -> str:
        return str(self.user)
