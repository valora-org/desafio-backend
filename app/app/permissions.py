from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, "is_admin"):
            if request.user.is_admin:
                return True
        else:
            return False
