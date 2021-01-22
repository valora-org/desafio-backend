from .permissions import IsAdmin
from .permissions import IsPlayer


class PlayerReadOnlyAdminWritePermissionMixin:
    """Grants permission for read/write for admin users and read for player."""

    def get_permissions(self):
        """Get permissions for access."""
        if self.action in ['list', 'retrieve']:
            aditional_permissions = IsPlayer | IsAdmin
        else:
            aditional_permissions = IsAdmin
        user_permissions = [*self.permission_classes, aditional_permissions]
        return [permission() for permission in user_permissions]
