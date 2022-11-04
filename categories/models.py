from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class Category(models.Model):
    class Meta:
        verbose_name_plural = _('Categories')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self) -> str:
        return '<Category %s - %s>' % (self.id, self.name)
