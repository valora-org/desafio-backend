from django.contrib import admin
from .models import Question, Answer, Quiz, Score


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Score)
