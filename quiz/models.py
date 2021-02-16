from django.db import models
from django.conf import settings


class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}, {self.text}'


class Quiz(models.Model):
    questions = models.ManyToManyField(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True)


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
