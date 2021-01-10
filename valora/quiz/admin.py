from django.contrib import admin
from quiz.models import Question
from django.contrib import admin

from quiz.models import Question

#
#
# # admin.site.unregister(Question)
# # admin.site.register(Question, Category)
#
#
# class TestInline(nested_admin.NestedTabularInline):
# 	model = Test
# 	extra = 4
# 	max_num = 4
#
#
# class QuestionInline(nested_admin.NestedTabularInline):
# 	model = Question
# 	inlines = [TestInline,]
# 	extra = 10
#
#
# class QuizAdmin(nested_admin.NestedModelAdmin):
# 	inlines = [QuestionInline,]

admin.site.register(Question)
