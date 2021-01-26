from django.db import models
from django.utils.translation import gettext_lazy as _

from quiz.categories.models import Category
from quiz.core.events.new_user import subscribe as subscribe_new_user
from quiz.users.models import User


class Profile(models.Model):
    """Player profile model."""

    player = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Get string representation."""
        return self.username

    @property
    def general_score(self):
        """Get general score."""
        return sum((cs.score for cs in self.category_scores.all()))

    @property
    def username(self):
        """Username of profile player."""
        return self.player.username

    @property
    def name(self):
        """Name of profile player."""
        return self.player.name

    @classmethod
    def handle_new_user(cls, user: User):
        """Handle a new user and create a profile if it is a player."""
        if user.role == User.Role.PLAYER:
            cls.objects.create(player=user)


subscribe_new_user(Profile.handle_new_user)


class CategoryScore(models.Model):
    """Score of a player at given category."""

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='category_scores')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Question ctegories'))
    score = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta info for category score model."""

        unique_together = ['profile', 'category']

    def __str__(self):
        """Get string representation."""
        return f'{self.profile.username} | {self.category.name}'

    def add_points(self, points):
        """Add points to score."""
        self.score = max(0, self.score + points)
        self.save()
