from django.urls import path

from categories.views import CategoryDetailView, CategoryView

app_name = 'category'

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path(
        '<str:category_id>/',
        CategoryDetailView.as_view(),
        name='category_detail',
    ),
]
