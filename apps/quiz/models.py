from django.db import models


class match(models.Model):
    OPTIONS = (
        ("1", "Answers One"),
        ("2", "Answers Two"),
        ("3", "Answers Three")
    )
    question = models.CharField(max_length=200, null=False, blank=False)
    answers_one = models.CharField(max_length=200, null=False, blank=False)
    answers_two = models.CharField(max_length=200, null=False, blank=False)
    answers_three = models.CharField(max_length=200, null=False, blank=False)
    correct_option = models.CharField(max_length=1, choices=OPTIONS, null=False, blank=False)
    player_response = models.CharField(max_length=1, choices=OPTIONS, null=False, blank=False)

    def __str__(self):
        return f'Correct: {self.correct_option} | {self.question}'

# class rank(models.Model):
#     rank_general = models.PositiveIntegerField
