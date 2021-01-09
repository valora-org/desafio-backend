from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
OPTIONS = (
    (1, 1),
    (2, 2),
    (3, 3)
)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Match(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    question = models.CharField(max_length=200, null=False, blank=False)
    answers_one = models.CharField(max_length=200, null=False, blank=False)
    answers_two = models.CharField(max_length=200, null=False, blank=False)
    answers_three = models.CharField(max_length=200, null=False, blank=False)
    correct_answers = models.CharField(max_length=1, choices=OPTIONS, null=False, blank=False)

    def __str__(self):
        return f'{self.question}'


class Selection(models.Model):
    id_question = models.ForeignKey(Match, on_delete=models.CASCADE)
    id_player = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    player_selection = models.CharField(max_length=1, choices=OPTIONS, null=False, blank=False)

    def __str__(self):
        return f'ID Player: {self.id_player} | Player Selection: {self.player_selection}'


class Rank(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    id_player = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    points = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f'ID Player: {self.id_player} | Point: {self.points}'
