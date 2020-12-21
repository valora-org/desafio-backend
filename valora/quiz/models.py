from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Question(models.Model):

    RIGHT_ANSWER = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    )

    category = models.ForeignKey(Category, related_name='question_category', on_delete=models.DO_NOTHING)
    question_text = models.CharField(max_length=400, blank=False, null=False)

    choice_A = models.CharField(max_length=200, blank=False, null=False)
    choice_B = models.CharField(max_length=200, blank=False, null=False)
    choice_C = models.CharField(max_length=200, blank=False, null=False)
    right_choice = models.CharField(max_length=1, choices=RIGHT_ANSWER, blank=False, null=False)

    def __str__(self):
        return '{0} - {1} - Correct: {2}'.format(self.category, self.question_text, self.right_choice)


class Answer(models.Model):

    ANSWER_CHOICES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    )

    category = models.ForeignKey(Category, related_name='answer_category', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answer_question', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    author_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES, blank=False, null=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        _answer = "Incorrect"
        if self.is_correct:
            _answer = "Correct"

        return "Result: {0} - {1} - {2}".format(self.question.id, self.author.username, _answer)


class Classification(models.Model):

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    points = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "Category: {0} - {1} : {2} points".format(self.category.name, self.author.username, self.points)

