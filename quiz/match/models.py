from typing import List, NamedTuple

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

from quiz.categories.models import Category
from quiz.questions.models import Question
from quiz.ranking.models import Profile


class MatchResponse(NamedTuple):
    """Simple representation for match response."""

    question: Question
    choice_index: int


class Match(models.Model):
    """Match model."""

    # Player cannot have more than one open match
    player = models.OneToOneField(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Not the best way to store questions, but this model is not accessible
    # outside.
    questions_ids = ArrayField(models.PositiveIntegerField(),
                               size=10,
                               null=True)

    def __str__(self):
        """Return a string representation for match instance."""
        return self.player.username

    @property
    def questions(self):
        """Get questions instances."""
        return [Question.objects.get(id=qid) for qid in self.questions_ids]

    def get_shuffle_questions(self, quantity=10):
        """Get shuffle questions on given quantity."""
        questions = Question.objects.filter(
            categories=self.category).order_by('?')[:quantity]
        self.questions_ids = [q.id for q in questions]
        self.save_questions_ids(questions)
        return questions

    def save_questions_ids(self, questions):
        """Save questions ids."""
        self.questions_ids = [question.id for question in questions]
        self.save()

    def add_to_ranking_profile(self, points):
        """Add match score to ranking profile."""
        profile = Profile.objects.get(player=self.player)
        category_score, _ = profile.category_scores.get_or_create(
            profile=profile, category=self.category)
        category_score.add_points(points)
        return profile.general_score

    def check_responses(self, responses: List[MatchResponse]):
        """Check given responses against the correct ones."""
        points = 0
        for response in responses:
            if response.question.correct_choice_index == response.choice_index:
                points += 1
            else:
                points -= 1
        points = max(0, points)
        general_score = self.add_to_ranking_profile(points)
        return points, general_score
