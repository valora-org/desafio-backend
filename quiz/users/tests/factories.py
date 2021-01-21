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
        password = (extracted if extracted else UserFactory.create_password())
        self.set_password(password)

    @classmethod
    def as_dict(cls, **kwargs):
        """Generate user information as dictionary."""
        return {
            'username': cls.username.generate(params={'locale': None}),
            'name': cls.name.generate(params={'locale': None}),
            'password': UserFactory.create_password(),
            'role': cls.role.fuzz(),
            **kwargs
        }

    @staticmethod
    def create_password():
        """Create a strong password."""
        return Faker(
            'password',
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(params={'locale': None})

    class Meta:
        """Metaclass for factory configuration."""

        model = User
        django_get_or_create = ['username']
