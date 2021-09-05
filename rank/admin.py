from django.contrib import admin

from rank.models import Rank


@admin.register(Rank)
class QuestionAdmin(admin.ModelAdmin):
    model = Rank
    list_display = ["id", "score", "category", "profile"]
    search_fields = ["profile"]
