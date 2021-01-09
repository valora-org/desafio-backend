from django.contrib import admin
from apps.quiz.models import Match, Category, Selection


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_category', 'question', 'answers_one',
                    'answers_two', 'answers_three', 'correct_answers')
    list_display_links = ('id', 'question')


admin.site.register(Match, MatchAdmin)


class SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_question', 'id_player', 'player_selection')
    list_display_links = ('id', 'id_question')


admin.site.register(Selection, SelectionAdmin)
