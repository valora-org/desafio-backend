from django.urls import path

from users import views as v

urlpatterns = [
    path("", v.get_users, name="users"),
]
