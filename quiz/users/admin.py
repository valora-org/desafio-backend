from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """Admin page for user model."""

    list_display = ['username', 'name', 'role']
    list_filter = ['role']
    search_fields = ['name', 'username', 'role']
