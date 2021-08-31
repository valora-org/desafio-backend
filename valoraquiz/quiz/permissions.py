from rest_framework import permissions

import users.choices


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return bool(request.user and (request.user.type == users.choices.ADMIN))
