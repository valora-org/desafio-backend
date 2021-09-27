from django.contrib import admin

from .models import Usuario, Pergunta, Resposta, Categoria, Quiz

admin.site.register(Usuario)

admin.site.register(Pergunta)

admin.site.register(Quiz)

admin.site.register(Resposta)

admin.site.register(Categoria)