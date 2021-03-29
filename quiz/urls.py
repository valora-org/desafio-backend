from django.urls import path
from .views import (RegisterQuizView,
                    RegisterCategoryView,
                    RetrieveQuizView,
                    ListQuizView,
                    DeleteQuizView,
                    StartQuizView,
                    UpdateQuizView,
                    DeleteCategoryView,
                    UpdateCategoryView,
                    FinishQuizView,)

app_name = "api-quiz"

urlpatterns = [
    path('register_quiz', RegisterQuizView.as_view(), name='register_quiz'),
    path('register_category', RegisterCategoryView.as_view(), name='register_category'),
    path('list_quiz', ListQuizView.as_view(), name='list_quiz'),
    path('start_quiz/category/<int:category>', StartQuizView.as_view(), name='start_quiz'),
    path('retrieve_quiz/<int:id>', RetrieveQuizView.as_view(), name='retrieve_quiz'),
    path('delete_quiz/<int:id>', DeleteQuizView.as_view(), name='delete_quiz'),
    path('update_quiz/<int:id>', UpdateQuizView.as_view(), name='update_quiz'),
    path('update_category/<int:id>', UpdateCategoryView.as_view(), name='update_category'),
    path('delete_category/<int:id>', DeleteCategoryView.as_view(), name='delete_category'),
    path('finish_quiz', FinishQuizView.as_view(), name='finish_quiz'),
]