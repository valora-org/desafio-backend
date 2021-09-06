from django.contrib import admin

from questions.models import Category, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ["id", "category", "registered_by", "is_active"]
    search_fields = ["category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["id", "name", "is_active"]
    search_fields = ["name"]
