from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Quiz(models.Model):

		##quiz modelQuiz model to store all the data related to the quiz.
		#Each quiz has its name, slug, timestamp and image
		#roll_out to allow you to edit the quiz without it appearing on the website..

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

		#Question model to store all the data related to the question.
		#Each question is linked to an individual quiz.
		#Every question has its label.

	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.label


class Answer(models.Model):

		#Answer model to store all the data related to the answer.
		#Each answer is linked to an individual question.
		#Each answer has its label and a correct answer parameter.

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.label


class QuizTaker(models.Model):

		#QuizTaker model to store all the data related to the quiz taker.
		#Each QuizTaker is linked to an individual user and to an individual quiz.
		#Each QuizTaker has its score

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	date_finished = models.DateTimeField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.email



class UsersAnswer(models.Model):

		#UsersAnswer model to store all the data related to the users answer.
		#Users Answer is linked to an individual quiz taker, to an individual question 
		#and to an individual answer.

	quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.question.label


@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)