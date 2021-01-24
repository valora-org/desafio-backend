from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Administration page for question model."""

    list_display = ['statement', 'id']
    search_fields = ['statement', 'id']
