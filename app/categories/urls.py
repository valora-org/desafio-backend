from django.urls import re_path
from categories.views import CategoryViewSet


category_update_delete_viewset = CategoryViewSet.as_view(
    {
        "delete": "destroy",
        "put": "update",
    }
)

app_name = "categories"
urlpatterns = [
    re_path(r"^category/$",
            CategoryViewSet.as_view({"post": "create"}), name="create_category"),
    re_path(r"^category/(?P<pk>\d+)/$", category_update_delete_viewset,
            name="update_delete_category"),
    re_path(r"^categories/$",
            CategoryViewSet.as_view({"get": "list"}), name="list_categories"),
]
