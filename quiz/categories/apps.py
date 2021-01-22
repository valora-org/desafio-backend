from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    """App config for categories."""

    name = 'quiz.categories'
    verbose_name = _('Categories')
