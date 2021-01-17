from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Category(models.Model):
	"""
		Category model to store data related to the categories.
		Each category has its title.

	"""

	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Quiz(models.Model):
	"""
		Quiz model to store all the data related to the quiz.
		Each quiz has its name, slug and timestamp.

	"""
	name = models.CharField(max_length=100)
	slug = models.SlugField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['timestamp',]
		verbose_name_plural = "Quizzes"

	def __str__(self):
		return self.name


class Question(models.Model):
	"""
		Question model to store all the data related to the question.
		Each question is linked to an individual quiz.
		Every question has its label.
 
	"""
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	
	def __str__(self):
		return self.label


class Answer(models.Model):
	"""
		Answer model to store all the data related to the answer.
		Each answer is linked to an individual question.
		Each answer has its label and a correct answer parameter.
 
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.label


class SubmitPlayer(models.Model):
	"""
		SubmitPlayer model to store all the data related to the submit player.
		Each submit player is linked to an individual user and to an individual quiz.
		Each submit player has its score.
 
	"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	
	def __str__(self):
		return self.user.username


class PlayersAnswer(models.Model):
	"""
		PlayersAnswer model to store all the data related to the answers players.
		Answers players is linked to an individual submit player, to an individual question 
			and to an individual answer.
 
	"""
	submit_player = models.ForeignKey(SubmitPlayer, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.question.label



# Notification for changing the slug quiz
@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)
