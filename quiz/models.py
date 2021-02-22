from django.db import models
from django.conf import settings


class QuestionQuerySet(models.QuerySet):
    def random_questions(self, category_slug):
        """ Manager para pegar perguntas aleatórias.
            Talvez não seja a forma mais eficiente, mas funciona para
            esse caso de uso.
        """
        return self.filter(category__slug=category_slug).order_by('?')[:10]


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
    objects = QuestionQuerySet.as_manager()

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
    answers = models.ManyToManyField(Answer, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)
    ended = models.BooleanField(default=False)


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
