from django.db.models import base
from django.urls import include, path
from rest_framework import routers
from user_auth.views import *
from quiz.views import *

router = routers.SimpleRouter()
router.register('quiz',QuizViewset,basename='quiz')
router.register('rank',RankViewset,basename='rank')

urls = router.urls

