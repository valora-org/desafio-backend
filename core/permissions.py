from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

from accounts.models import Account


class IsAdminAccount(BasePermission):
    def has_object_permission(self, request: Request, _, obj: Account):
        if request.user.is_superuser:
            return True

        return obj == request.user


class IsAdminOrReadOnlyAccount(BasePermission):
    def has_permission(self, request: Request, _):
        if request.method in SAFE_METHODS:
            return request.user.is_superuser

        return True


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, _):
        ADMINS_ONLY = (
            'POST',
            'PATCH',
            'PUT',
            'DELETE',
        )
        if request.method in ADMINS_ONLY:
            return request.user.is_superuser

        return True
