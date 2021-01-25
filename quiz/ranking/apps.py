from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RankingConfig(AppConfig):
    """App config for ranking."""

    name = 'quiz.ranking'
    verbose_name = _('Ranking')
