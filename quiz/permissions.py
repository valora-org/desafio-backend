from rest_framework import permissions
from users.models import User


class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type == User.ADMIN
