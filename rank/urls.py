from django.urls import path

from rank import views as r

urlpatterns = [
    path(
        "",
        r.get_rank,
        name="rank",
    ),
    path(
        "user/",
        r.get_rank_by_user,
        name="user-rank",
    ),
    path(
        "user/<str:pk>/",
        r.get_rank_by_category,
        name="category-rank",
    ),
]
