from django.urls import path, include
from desafiobackend.quiz import api

app_name = 'quiz'

urlpatterns = [
    path('api/', include('desafiobackend.quiz.api.urls')),
]
