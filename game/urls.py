
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='Category')
router.register(r'questions',views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

router.register(r'quizpage', views.QuizPageViewSet)
router.register(r'quiz', views.QuizViewSet)


router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
