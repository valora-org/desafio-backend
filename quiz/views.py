import reversion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render

from quiz import models


@login_required
@transaction.atomic
# @reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def quiz(request, quiz_id):
    quiz = models.Quiz.objects.get(id=quiz_id)
    questions = models.Question.objects.filter(quiz=quiz)
    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz/quiz.html', context)
