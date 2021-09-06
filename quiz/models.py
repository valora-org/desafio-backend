from django.db import models


class Quiz(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True, related_name='quiz')
    score = models.IntegerField(default=0)
    category = models.CharField(max_length=100)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
