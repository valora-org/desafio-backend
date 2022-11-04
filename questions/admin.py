from django.contrib import admin

from answers.models import Answer
from questions.models import Question


class AnswerModel(admin.TabularInline):
    model = Answer
    fields = (
        'answer',
        'is_correct',
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at')
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'id',
                    'question',
                    'level',
                    'created_at',
                    'is_active',
                    'quiz',
                )
            },
        ),
    )

    list_display = (
        'id',
        'question',
        'level',
        'created_at',
        'quiz',
    )

    inlines = (AnswerModel,)
