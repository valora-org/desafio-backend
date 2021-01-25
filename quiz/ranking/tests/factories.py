from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from quiz.categories.tests.factories import CategoryFactory
from quiz.ranking.models import CategoryScore, Profile
from quiz.users.tests.factories import UserFactory


class ProfileFactory(DjangoModelFactory):
    """Factory for profile model."""

    player = SubFactory(UserFactory)

    class Meta:
        """Meta class for profile factory."""

        model = Profile


class CategoryScoreFactory(DjangoModelFactory):
    """Factory for category score model."""

    profile = SubFactory(ProfileFactory)
    category = SubFactory(CategoryFactory)
    score = Faker('pyint', min_value=0, max_value=500)

    class Meta:
        """Meta class for category score factory."""

        model = CategoryScore
