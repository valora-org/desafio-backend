from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission, BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Fully featured User model with admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    TYPES_CHOICES = (
        ("1", _("Admin")),
        ("2", _("Player")),
    )

    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    current_quizz = models.JSONField(verbose_name="Quizz Atual", blank=True)
    ranking_points = models.IntegerField(verbose_name="Pontos do Ranking", default=0)
    user_type = models.CharField(verbose_name="Tipo de Usuário", default="2", blank=True, choices=TYPES_CHOICES, max_length=50)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def set_current_quizz(self, quizz):
        self.current_quizz = quizz
        self.save()

    def get_current_quizz_question(self):
        return self.current_quizz