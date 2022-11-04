from django.contrib import admin

from .models import Category


@admin.register(Category)
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
