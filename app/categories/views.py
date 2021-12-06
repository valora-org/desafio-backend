from rest_framework import viewsets, permissions

from app.permissions import IsAdmin

from categories.models import Category
from categories.serializers import CategorySerializer


# Category View with support for create, update, delete and
# list categories. Permission varies depending on the method.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated, IsAdmin],
        "update": [permissions.IsAuthenticated, IsAdmin],
        "delete": [permissions.IsAuthenticated, IsAdmin],
        "list": [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # if action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
