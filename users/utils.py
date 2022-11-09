from django.contrib.auth.models import BaseUserManager
from rest_framework import permissions


class CustomUserManager(BaseUserManager):
    """
    Modified django BaseUser to set email as pk
    """

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        # Leave if the user to be create doesn't have an email
        if not email:
            raise ValueError("An email must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Is_admin_or_read(permissions.BasePermission):
    """
    Allow only admins or safe methods
    """

    def has_permission(self, request, _):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_superuser
