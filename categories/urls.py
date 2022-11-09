from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryView.as_view()),
    path("categories/<int:category_id>/", views.CategorySoloView.as_view()),
]
