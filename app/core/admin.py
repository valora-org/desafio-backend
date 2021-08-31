from django.contrib import admin

from .models import CategoryModel, AnswerModel, QuestionModel

admin.site.register(CategoryModel)
admin.site.register(AnswerModel)
admin.site.register(QuestionModel)
