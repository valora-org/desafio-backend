from factory import Faker
from factory.django import DjangoModelFactory

from quiz.categories.models import Category


class CategoryFactory(DjangoModelFactory):
    """Factory for category model."""

    name = Faker('pystr', min_chars=5, max_chars=50)

    @classmethod
    def as_dict(cls, **kwargs):
        """Generate category information as dictionary."""
        return {'name': cls.name.generate(params={'locale': None}), **kwargs}

    class Meta:
        """Meta class for category factory."""

        model = Category
