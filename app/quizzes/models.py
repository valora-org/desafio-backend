from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=250, blank=True)
    question = models.ForeignKey(
        "quizzes.Question", on_delete=models.CASCADE, related_name="answers")
    is_correct = models.BooleanField(default=False)


class Question(models.Model):
    question_text = models.CharField(max_length=250, blank=True)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE)


class Ranking(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    score = models.IntegerField(default=0, blank=True)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE)
