from rest_framework import permissions


# Check if user has admin permission. Return True if user does, else False
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, "is_admin"):
            if request.user.is_admin:
                return True
        else:
            return False
