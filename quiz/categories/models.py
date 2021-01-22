from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Category model."""

    name = models.CharField(_('Category name'), max_length=100,
                            blank=False, unique=True, null=False,
                            help_text=_('Name of category'))

    class Meta:
        """Meta info for category model."""

        verbose_name = _('category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self) -> str:
        """Return a string representation for category instance."""
        return self.name

    @property
    def questions_count(self):
        """Quantity of questions from category."""
        # TODO: implement after create questiosn app.
        return -1
