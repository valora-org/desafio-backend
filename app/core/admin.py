from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CategoryModel, AnswerModel, QuestionModel, CategoryQuestionModel, UserModel,
    RankingModel
)

admin.site.register(UserModel, UserAdmin)
admin.site.register(CategoryModel)
admin.site.register(QuestionModel)
admin.site.register(CategoryQuestionModel)
admin.site.register(AnswerModel)
admin.site.register(RankingModel)