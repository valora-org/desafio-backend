from django.urls import path

from categories import views

urlpatterns = [
    path('', views.CategoryView.as_view(), name='list-create-category'),
    path(
        '<str:id>/',
        views.CategoryDetailView.as_view(),
        name='category-detail',
    ),
]
