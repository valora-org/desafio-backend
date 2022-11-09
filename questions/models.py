from django.db import models


class Question(models.Model):
    description = models.CharField(max_length=255)
    answer = models.IntegerField()


class Alternative(models.Model):
    description = models.CharField(max_length=255)

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="alternatives"
    )
