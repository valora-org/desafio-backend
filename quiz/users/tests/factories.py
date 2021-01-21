from typing import Any
from typing import Sequence

from factory import Faker
from factory import post_generation
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from quiz.users.models import User


class UserFactory(DjangoModelFactory):
    """Test factory for user model."""

    username = Faker('user_name')
    name = Faker('name')
    role = FuzzyChoice(
        choices=[c[0] for c in User.Role.choices if c != User.Role.SUPERUSER],)

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        """Create a password for user instance."""
        password = (extracted if extracted else Faker(
            'password',
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(params={'locale': None}))
        self.set_password(password)

    class Meta:
        """Metaclass for factory configuration."""
        model = User
        django_get_or_create = ['username']
