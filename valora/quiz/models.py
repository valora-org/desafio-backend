from django.db import models

from quiz.choices import CORRECT


class Category(models.Model):
    category = models.CharField(verbose_name=("category"), max_length=250, blank=True, unique=True, null=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return f'Category={self.category}'


class Question(models.Model):
    category = models.ForeignKey('Category', related_name='question_category', on_delete=models.CASCADE)
    question = models.CharField(max_length=700, blank=False, null=False, verbose_name='Question')
    option_a = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option A')
    option_b = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option B')
    option_c = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option C')
    correct = models.CharField(max_length=2, blank=False, null=False, choices=CORRECT)
    correct_user = models.CharField(max_length=2, blank=True, null=True, choices=CORRECT)

    class Meta:
        verbose_name = ("Questão")
        verbose_name_plural = ("Questões")

    def __str__(self):
        return self.question

