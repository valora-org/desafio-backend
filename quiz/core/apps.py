from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    """App config for core."""

    name = 'quiz.core'
    verbose_name = _('Core')
