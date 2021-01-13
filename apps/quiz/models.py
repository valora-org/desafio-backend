from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
OPTIONS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
)


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class MatchGame(models.Model):
    category_id = models.ForeignKey(Category, related_name='match_game', on_delete=models.CASCADE)

    question = models.CharField(max_length=200)
    answers_one = models.CharField(max_length=200)
    answers_two = models.CharField(max_length=200)
    answers_three = models.CharField(max_length=200)
    correct_answers = models.CharField(max_length=1, choices=OPTIONS)

    class Meta:
        ordering = ['id']
        # quizzes cannot be repeated
        unique_together = ['question', 'answers_one', 'answers_two', 'answers_three']

    def __str__(self):
        return f'{self.question}'


class Selection(models.Model):
    match_game_id = models.ForeignKey(MatchGame, on_delete=models.CASCADE)
    player_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    player_selection = models.CharField(max_length=1, choices=OPTIONS)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'ID Player: {self.player_id} | Player Selection: {self.player_selection}'


class Rank(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    player_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'ID Player: {self.player_id} | Point: {self.points}'
