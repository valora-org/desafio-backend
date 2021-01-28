from django.contrib import admin

# Register your models here.
from .models import Classificacao, Pergunta

admin.site.register(Classificacao)
admin.site.register(Pergunta)