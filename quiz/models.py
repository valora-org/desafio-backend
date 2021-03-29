from django.db import models

ANSWER_METHOD = ['a', 'b', 'c', 'A', 'B', 'C']


class LetterAnswers(models.TextChoices):
    letter_a = 'A', 'A'
    letter_b = 'B', 'B'
    letter_c = 'C', 'C'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=300)
    answer_A = models.CharField(max_length=200, verbose_name="Letra A")
    answer_B = models.CharField(max_length=200, verbose_name="Letra B")
    answer_C = models.CharField(max_length=200, verbose_name="Letra C")
    correct_letter = models.CharField(
        max_length=1,
        choices=LetterAnswers.choices,
        verbose_name='Correct Answer'

    )


class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name="Quiz Title")
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quiz"

    def __str__(self):
        return self.title