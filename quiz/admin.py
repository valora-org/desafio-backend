from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Quiz, Question
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

@admin.register(Quiz)
class QuizAdmin(VersionAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(VersionAdmin):
    pass

