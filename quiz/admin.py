from django.contrib import admin
from reversion.admin import VersionAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User, Quiz, Question, Answer

admin.site.register(User, UserAdmin)

@admin.register(Quiz)
class QuizAdmin(VersionAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(VersionAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(VersionAdmin):
    pass
