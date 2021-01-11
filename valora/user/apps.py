from django.apps import AppConfig
from import_export.admin import ImportExportModelAdmin


class UserConfig(AppConfig):
    name = 'user'


class ProfileAdmin(ImportExportModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'points',)
