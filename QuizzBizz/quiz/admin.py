from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer, QuizTaker, UsersAnswer


class AnswerInline(nested_admin.NestedTabularInline):
	
	#Setting the number of answers for registration for single question.

	model = Answer
	extra = 3
	max_num = 3


class QuestionInline(nested_admin.NestedTabularInline):

	#Setting the number of questions for registration for single quiz.

	model = Question
	inlines = [AnswerInline,]
	extra = 3


class QuizAdmin(nested_admin.NestedModelAdmin):

	#Setting admin for quiz.


	inlines = [QuestionInline,]


class UsersAnswerInline(admin.TabularInline):

	#Setting admin for users.

	model = UsersAnswer


class QuizTakerAdmin(admin.ModelAdmin):

	#Configuring admin for player submissions.

	inlines = [UsersAnswerInline,]



# Registers


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(UsersAnswer)