from django.urls import path

from quiz import views

app_name = 'quiz'

urlpatterns = [

    path('category_adm/', views.CategoryAdminViewSet.as_view({'get': 'list'}), name='category-adm'),
    path('category_list/', views.CategoryViewSet.as_view({'get': 'list'}), name='category_list'),
    path('question_adm/', views.QuestionAdminViewSet.as_view({'get': 'list'}), name='question-adm'),
    path('<int:category_id>/', views.StartQuiz.as_view(), name='start'),
]