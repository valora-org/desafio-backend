from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """App config for users."""
    name = 'quiz.users'
    verbose_name = _('Users')
