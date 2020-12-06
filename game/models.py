from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category

class Question(models.Model):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    isCorrect = models.BooleanField()

    def __str__(self):
        return self.answer

class QuizPage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.question
