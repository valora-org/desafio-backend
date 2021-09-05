from rest_framework import permissions


class PlayerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Usuários do tipo player podem somente listar as categorias dentro da
        view Category
        Usuários do tipo player podem fazer as operações permitidas no quiz e
        também do ranking
        Usuários admin podem fazer todas as operações
        """
        view_name = view.get_view_name().replace(' ','_')
        view_name = view_name.lower()
        if view_name == 'category_list':
            if request.user and request.user.is_authenticated:
                return True
        if view_name == 'category_instance':
            if (
                request.user and
                request.user.is_authenticated and
                request.user.is_superuser
            ):
                return True
            else:
                return False
        if request.user and request.user.is_authenticated:
            return True
        return False