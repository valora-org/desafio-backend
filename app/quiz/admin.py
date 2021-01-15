from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer, SubmitPlayer, PlayersAnswer


class AnswerInline(nested_admin.NestedTabularInline):
	"""
		Setting the number of answers for registration for single question.

	"""
	model = Answer
	extra = 3
	max_num = 3


class QuestionInline(nested_admin.NestedTabularInline):
	"""
		Setting the number of questions for registration for single quiz.

	"""
	model = Question
	inlines = [AnswerInline,]
	extra = 10


class QuizAdmin(nested_admin.NestedModelAdmin):
	"""
		Setting admin for quiz.

	"""
	inlines = [QuestionInline,]


class PlayersAnswerInline(admin.TabularInline):
	"""
		Setting admin for players.

	"""
	model = PlayersAnswer


class SubmitPlayerAdmin(admin.ModelAdmin):
	"""
		Configuring admin for player submissions.

	"""
	inlines = [PlayersAnswerInline,]

# Registers
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SubmitPlayer, SubmitPlayerAdmin)
admin.site.register(PlayersAnswer)
