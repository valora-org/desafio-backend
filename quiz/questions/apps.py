from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuestionsConfig(AppConfig):
    """App config for questions."""

    name = 'quiz.questions'
    verbose_name = _('Questions')
