from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(_("category name"), max_length=50)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    text = models.CharField(_("question"), max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(_("active"), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        max_length = 50
        return f"{self.text[:max_length]}"
    
class Quiz(models.Model):
    name = models.CharField(_("quiz name"), default=_("New Quiz"), max_length=150, unique=True)
    question = models.ManyToManyField(Question, verbose_name=_("questions"), blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = 'quiz'
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return f"{self.name}"

class Answer(models.Model):
    text = models.CharField(_("answer"), max_length=255)
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    is_correct = models.BooleanField(_("correct answer"), default=False)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'

    def __str__(self):
        return f"{self.text}"