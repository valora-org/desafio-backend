from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    enunciation = models.TextField()    

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.enunciation


class Category(models.Model):
    title = models.CharField(max_length=50)
    questions = models.ManyToManyField(Question)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

class Option(models.Model):
    description = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        return f"question: {self.question.pk}, answer: {self.description}, correct: {self.is_correct}"


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name='questions')
    is_finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

    @property
    def accepts(self):
        return Answer.objects.filter(quiz=self, option__is_correct=True).count()

    @property
    def faults(self):
        return Answer.objects.filter(quiz=self, option__is_correct=False).count()

    @property
    def score(self):
        accepts = self.accepts
        faults = self.faults
        result = accepts - faults
        
        return result if result >= 0 else 0

    def __str__(self):
        return f"Category: {self.category} - {self.user}"


class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='answer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return f"question: {self.option.question.pk}, answer: {self.option.pk} - {self.option.description}, correct: {self.option.is_correct}"

    