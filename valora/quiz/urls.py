from django.urls import path
from .views import CategoryList, CategoryDetail, QuestionList, QuestionDetail
from .views import get_question_list_by_category
from .views import AnswerList
from .views import get_answer_list_by_category
from .views import get_answer_list_by_user
from .views import get_ranking

urlpatterns = [

    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_list'),

    path('question/', QuestionList.as_view(), name='questions_list'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='questions_detail'),
    path('question/category/<int:_id>/', get_question_list_by_category, name='questions_category_list'),

    path('answer/', AnswerList.as_view(), name='answer_list'),
    path('answer/category/<int:_id>/', get_answer_list_by_category, name='answer_category_list'),
    path('answer/author/<int:_id>/', get_answer_list_by_user, name='answer_author_list'),

    path('ranking/', get_ranking, name='overall_ranking'),
    path('ranking/category/<int:_id>/', get_ranking, name='category_ranking'),
]
