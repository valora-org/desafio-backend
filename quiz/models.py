from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

        
class Quiz(models.Model):
    CATEGORY = [
        (0, _('Music')),
        (1, _('Sports')),
        (2, _('News')),
        (3, _('Television')),
        (4, _('History')),
        (5, _('Science')),
        (6, _('Fiction')),
        (7, _('Art')),
        (8, _('Math')),
        (9, _('Animals')),
        (10, _('Anagrams')),
    ]

    # user = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0, verbose_name=_("Score"))
    category = models.PositiveSmallIntegerField(choices=CATEGORY, verbose_name=_("Category"), default=0)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, verbose_name=_("Question"), blank=True)
    true_answer = models.PositiveSmallIntegerField(verbose_name=_("True Answer"), default=0)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name=_("Answer"), blank=True)
    
class Player(User):
    admin = models.BooleanField(default=False, verbose_name=_("Player Admin"))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.username