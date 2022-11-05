from django.contrib import admin

from answers.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'id',
                    'answer',
                    'is_correct',
                    'question',
                )
            },
        ),
    )
    list_display = (
        'id',
        'answer',
        'is_correct',
        'question',
    )
