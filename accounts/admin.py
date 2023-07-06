from django.contrib import admin
from accounts.models import CustomUser as User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'username', 'score', 'is_staff')