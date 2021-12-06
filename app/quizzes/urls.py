from django.urls import re_path
from quizzes.views import AnswerViewSet, QuestionViewSet, RankingViewSet, GetQuizViewSet


answer_update_delete_viewset = AnswerViewSet.as_view(
    {
        "delete": "destroy",
        "put": "update",
    }
)

question_update_delete_viewset = QuestionViewSet.as_view(
    {
        "delete": "destroy",
        "put": "update",
    }
)

app_name = "quizzes"
urlpatterns = [
    re_path(r"^answer/$",
            AnswerViewSet.as_view({"post": "create"}), name="create_answer"),
    re_path(r"^answer/(?P<pk>\d+)/$", answer_update_delete_viewset,
            name="update_delete_answer"),
    re_path(r"^answers/$",
            AnswerViewSet.as_view({"get": "list"}), name="list_answers"),
    re_path(r"^question/$",
            QuestionViewSet.as_view({"post": "create"}), name="create_question"),
    re_path(r"^question/(?P<pk>\d+)/$", question_update_delete_viewset,
            name="update_delete_question"),
    re_path(r"^questions/$",
            QuestionViewSet.as_view({"get": "list"}), name="list_questions"),
    re_path(r"^get-quiz/$",
            GetQuizViewSet.as_view({"get": "get_quiz"}), name="get_quiz"),
    re_path(r"^finish-quiz/$",
            RankingViewSet.as_view({"post": "create"}), name="create_entry_to_ranking"),
    re_path(r"^ranking/$",
            RankingViewSet.as_view({"get": "list"}), name="list_ranking"),
]
