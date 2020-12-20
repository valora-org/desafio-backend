from django.contrib import admin

from .models import Category, Question, Answer, Classification

admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Classification)