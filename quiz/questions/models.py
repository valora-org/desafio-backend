from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.validators import ArrayMinLengthValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from quiz.categories.models import Category


class Question(models.Model):
    """Question model."""

    categories = models.ManyToManyField(Category, related_name='questions',
                                        verbose_name=_('Question ctegories'),
                                        help_text=_('Question ctegories'))

    statement = models.CharField(_('Question statement'), max_length=255,
                                 blank=False, null=False,
                                 help_text=_('Question statement'))

    # This field takes advantage of using Postgres database
    choices = ArrayField(models.CharField(max_length=255, blank=False),
                         size=3,
                         validators=[ArrayMinLengthValidator(3)])

    correct_choice_index = models.PositiveIntegerField(
        null=False, validators=[MaxValueValidator(2)])

    def __str__(self) -> str:
        """Return a string representation for question instance."""
        return self.statement[:20]
