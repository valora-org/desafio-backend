from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    admin = models.BooleanField(default=False, blank=False, null=False, verbose_name=_('Admin'))
    score = models.PositiveSmallIntegerField(default=0, verbose_name=_("Score"))

    def __str__(self):
        return self.username

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

    user = models.ManyToManyField(User, verbose_name=_("User"))
    category = models.PositiveSmallIntegerField(choices=CATEGORY, verbose_name=_("Category"), default=0)

    def __str__(self):
        print(self.user)
        print(dir(self.user))
        return str(self.user.name + ": " + self.CATEGORY[self.category][-1])

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    question = models.CharField(max_length=200, verbose_name=_("Question"), blank=False, null=False, default="Type an question")
    correct_answer = models.PositiveSmallIntegerField(verbose_name=_("Correct Answer"), default=0, null=False,)
    user_answer = models.PositiveSmallIntegerField(verbose_name=_("User Answer"), default=0, blank=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=200, verbose_name=_("Answers"), blank=False, null=False, default="Type an answer")

    def __str__(self):
        return self.user.name + ": " + self.user_answers

