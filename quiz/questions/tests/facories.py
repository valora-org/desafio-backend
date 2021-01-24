from random import randint

from factory import Faker, List, post_generation
from factory.django import DjangoModelFactory

from quiz.categories.tests.factories import CategoryFactory
from quiz.questions.models import Question


class QuestionFactory(DjangoModelFactory):
    """Factory for question model."""

    statement = Faker('sentence', nb_words=20)
    choices = List([Faker('sentence', nb_words=20) for _ in range(3)])
    correct_choice_index = Faker('pyint', min_value=0, max_value=3)

    @post_generation
    def categories(self, create, extracted, **kwargs):
        """Create categories or use the received ones."""
        if extracted:
            values = extracted
        else:
            values = [CategoryFactory() for _ in range(randint(1, 10))]
        for category in values:
            self.categories.add(category)

    @classmethod
    def as_dict(cls, **kwargs):
        """Generate question information as dictionary."""
        return {
            'statement': cls.statement.generate(params={'locale': None}),
            'choices': [
                Faker('sentence', nb_words=20).generate(params={'locale': None})
                for _ in range(3)
            ],
            'correct_choice_index': randint(0, 2),
            'categories': [CategoryFactory().id for _ in range(randint(1, 10))],
            **kwargs
        }

    class Meta:
        """Meta class for question factory."""

        model = Question
