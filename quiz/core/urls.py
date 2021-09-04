from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quiz.core import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
]
