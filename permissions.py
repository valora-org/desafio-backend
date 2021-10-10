from rest_framework.permissions import BasePermission

class IsPlayerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser == False


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

