from django.contrib import admin
from desafiobackend.quiz.models import Category, Quiz, Question, Answer, Option


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
#admin.site.register(MarksOfUser)
admin.site.register(Answer)
admin.site.register(Category)


