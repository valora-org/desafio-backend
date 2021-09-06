from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Quiz, Question

@admin.register(Quiz)
class QuizAdmin(VersionAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(VersionAdmin):
    pass