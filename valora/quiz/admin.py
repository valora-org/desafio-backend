from django.contrib import admin

from .models import Category, Quiz, Results

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Results)
