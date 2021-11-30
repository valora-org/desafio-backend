from rest_framework.permissions import BasePermission
from rest_framework import permissions
from user_auth.models import Player

class IsSameUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return request.user.id == obj.id


class IsPlayer(BasePermission):
    def has_permission(self, request, view):
        auth = request.auth
        if auth is not None:
            return isinstance(request.user,Player)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        #TODO : get object type
        return isinstance(request.user,Player)

