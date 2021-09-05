from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from users.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    list_display = ["id", "email"]
    search_fields = ["email"]
