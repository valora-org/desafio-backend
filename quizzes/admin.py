from django.contrib import admin

from . import models


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
