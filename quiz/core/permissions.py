from rest_framework.permissions import BasePermission
from rest_framework.settings import api_settings

from quiz.users.models import User


class IsAdmin(BasePermission):
    """Permission for admin user."""

    def has_permission(self, request, view):
        """Check permission for request user if it has the admin role."""
        user = request.user
        return user.role == User.Role.ADMIN[0]


class IsPlayer(BasePermission):
    """Permission for player user."""

    def has_permission(self, request, view):
        """Check permission for request user if it has the player role."""
        user = request.user
        return user.role == User.Role.PLAYER[0]


# Default permissions
default_permissions = api_settings.DEFAULT_PERMISSION_CLASSES
