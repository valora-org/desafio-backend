from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

class Quiz(models.Model):

    #the quiz model to store 
    #the name of the quiz and virtually all the data 
    #related to the quiz. I also gave an option of roll_out 
    #to allow you to edit the quiz without it appearing on the website.


    name = models.CharField(max_length=100)
    description = models.CharField(max_length=70)
    image = models.ImageField()
    slug = models.SlugField(blank=True)
    roll_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp',]
        verbose_name_plural = "Quizzes"
    
    def __str__(self):
        return self.name


class Question(models.Model):

    #Each Question is linked to an individual 
    #Quiz in the sense that every question has its label. 
    #the question, and the quiz with which it belongs to. 

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Answer(models.Model):

    #As we all know every question must have an answer, 
    #although you can notice that there is also an extra field 
    #called is_correct. That is to specify whether that is the 
    #actual correct answer or not.

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class QuizTaker(models.Model):

    #Every time someone takes a quiz, 
    #a quiz taker instance is created to save which user took the test,
    #what the user scored in terms of correct answers, 
    #and whether the user has completed the quiz or not.

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz =  models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    date_finished = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserAnswer(models.Model):

    #These are just to make sure that the name of the quiz gets 
    #slugified and that the questions_count in the quiz is always 
    #equal to the number of questions related to that quiz.

    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question.label
