from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from user.models import UserProfile


# Register your models here.


@admin.register(UserProfile)
class ProfileAdmin(ImportExportModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'points',)
