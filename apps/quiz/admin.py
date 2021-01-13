from django.contrib import admin
from apps.quiz.models import MatchGame, Category, Selection


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'question', 'answers_one',
                    'answers_two', 'answers_three', 'correct_answers')
    list_display_links = ('id', 'question')


admin.site.register(MatchGame, MatchAdmin)


class SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_game_id', 'player_id', 'player_selection')
    list_display_links = ('id', 'match_game_id')


admin.site.register(Selection, SelectionAdmin)
