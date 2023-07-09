from django.contrib import admin
from quiz.models import Category, Answer, Quiz, Question

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AnswerAdmin(admin.TabularInline):
    """
    Enable answer model to be edited in other
    """
    model = Answer
    min_num = 3
    max_num = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    
    fields = ['text', 'quiz', 'is_active']
    list_display = ['text', 'quiz', 'is_active']
    inlines = [
        AnswerAdmin,
    ]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']
    

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'is_correct', 'question_id' ]