
from django.urls import path
from ranking import views

urlpatterns = [
    path('consult_global_ranking', views.GlobalRanking.as_view(), name="global_ranking"),
    path('consult_category_ranking', views.CategoryRanking.as_view(), name="global_ranking")
] 