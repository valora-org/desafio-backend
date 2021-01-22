from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Administration page for category model."""

    list_display = ['name', 'id']
    search_fields = ['name', 'id']
