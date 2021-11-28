import logging
from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from quiz.models.quiz import *
from quiz.models.question import *
from django.utils.safestring import mark_safe
from django.urls import reverse
from .forms import *

class OptionInlineAdmin(admin.TabularInline):
    model = Option
    # form = PhotographerChangeForm
    extra = 0
    min_num = 3
    max_num = 3

class QuestionAdmin(ModelAdmin):
    model = Question
    form = QuestionForm
    inlines = (OptionInlineAdmin,)
   
    list_display = ['id','enunciation','quiz']
    list_filter = ['id','quiz']

 
    def get_queryset(self, request):
     
        return super().get_queryset(request)


class QuizAdmin(ModelAdmin):
    model = Quiz
   
    list_display = ['id','category']
    list_filter = ['id']

 
    def get_queryset(self, request):
     
        return super().get_queryset(request)

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)