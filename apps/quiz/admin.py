from django.contrib import admin
from apps.quiz.models import Match


class matchs(admin.ModelAdmin):
    list_display = ('id', 'question', 'answers_one', 'answers_two', 'answers_three', 'player_response')
    list_display_links = ('id', 'question')


admin.site.register(Match, matchs)
