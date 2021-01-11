from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from quiz.models import Question, Category


@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    raw_id_fields = ('category',)
    list_display = ('category', 'question', 'correct',)


admin.site.register(Category)
