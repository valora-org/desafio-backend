from django.urls import path

from categories import views

app_name = 'category'

urlpatterns = [
    path('', views.CategoryView.as_view(), name='list-create-category'),
    path(
        '<str:category_id>/',
        views.CategoryDetailView.as_view(),
        name='category-detail',
    ),
]
