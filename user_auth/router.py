from rest_framework import routers
from user_auth.views import *
from quiz.views import *

router = routers.SimpleRouter()
router.register('players', PlayerViewset)

urls = router.urls