from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin

from .models import Account


class CustomAccountAdmin(UserAdmin):
    readonly_fields = (
        'date_joined',
        'last_login',
        'id',
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (
            'Personal Info',
            {'fields': ('first_name', 'last_name', 'username', 'id')},
        ),
        ('Access Info', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'is_superuser')


site.register(Account, CustomAccountAdmin)
