from django.urls import path

from questions import views as q

urlpatterns = [
    path("categories/", q.get_categories, name="categories"),
    path("create-category/", q.create_category, name="create-category"),
    path(
        "update-category/<str:pk>/",
        q.update_category,
        name="update-category",
    ),
    path(
        "delete-category/<str:pk>/",
        q.delete_category,
        name="delete-category",
    ),
]
