from django.utils.translation import gettext_lazy as _

from django_filters import rest_framework as filters

from rest_framework.viewsets import ModelViewSet

from quiz.core.viewmixins import PlayerReadOnlyAdminWritePermissionMixin

from .models import Category
from .serializers import CategorySerializer


class CategoryFilter(filters.FilterSet):
    """Filter for category."""

    name = filters.CharFilter(
        field_name='name', lookup_expr='icontains',
        help_text=_('Filter by any part of category name. Case insensitive'))

    class Meta:
        """Meta info for category filter."""

        model = Category
        fields = ['name']


class CategoryViewSet(PlayerReadOnlyAdminWritePermissionMixin, ModelViewSet):
    """Category endpoint.

    create:
    Create a new category.

    retrieve:
    Get a specific category information according to its id.

    list:
    Retrieve a paginated list of categoryies. Filter by any part of category
    name.

    update:
    Update an category information.

    partial_update:
    Partially update a category information.

    destroy:
    Delete a category.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_class = CategoryFilter
