from django.contrib import admin
from quizzes import models

admin.site.register(models.Question)
admin.site.register(models.Category)
