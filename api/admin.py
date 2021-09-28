from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Answer, Question, Quiz, Category
from .forms import UserCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login', 'is_admin')
        }),
        ('Permissões', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions'
            )
        }
         ),
    )
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'category', 'correct_answers', 'created', 'finish']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'category']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'is_right']

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
