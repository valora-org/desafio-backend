from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'id',
                    'name',
                )
            },
        ),
    )
    list_display = (
        'id',
        'name',
    )


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'created_at',
    )
    fieldsets = (
        ('Fields', {'fields': ('id', 'name', 'created_at', 'category')}),
    )

    list_display = (
        'id',
        'name',
        'created_at',
        'category',
    )


class AnswerModel(admin.TabularInline):
    model = models.Answer
    fields = (
        'answer',
        'is_correct',
    )


@admin.register(models.Question)
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


@admin.register(models.Answer)
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
