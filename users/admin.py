from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User

admin.site.register(User, auth_admin.UserAdmin)
