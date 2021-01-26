from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MatchConfig(AppConfig):
    """App config for matches."""

    name = 'quiz.match'
    verbose_name = _('Match')
    verbose_name_plural = _('Matches')
