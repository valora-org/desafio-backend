from rest_framework import views, permissions, status, viewsets

class MixedPermissionModelViewSet(viewsets.ModelViewSet):
    '''
    Mixed permission base model allowing for action level
    permission control. Subclasses may define their permissions
    by creating a 'permission_classes_by_action' variable.

    Example:
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdminUser]}
    '''

    permission_classes_by_action = {}

    def create(self, request, *args, **kwargs):
        return super(MixedPermissionModelViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(MixedPermissionModelViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super(MixedPermissionModelViewSet, self).retrieve(request, pk, *args, **kwargs)
        

    def update(self, request, pk=None, *args, **kwargs):
        return super(MixedPermissionModelViewSet, self).update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super(MixedPermissionModelViewSet, self).partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super(MixedPermissionModelViewSet, self).destroy(request, pk, *args, **kwargs)


    def get_permissions(self):
        try:
        # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
        # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
