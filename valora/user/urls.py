
from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    
    path('', views.RankingAPIView.as_view({'get': 'list'}) , name='ranking'),
    path('account', views.account_redirect, name='account-redirect'),
    path('ranking_category/<int:category_id>', views.RankingCategoryAPIView.as_view({'get': 'list'}), name='category-list'),
    path('temp_points', views.TempRankingAPIView.as_view({'get': 'list'}), name='temp_points'),

]
