from django_filters import rest_framework as filters

from rest_framework.viewsets import ModelViewSet

from quiz.core.permissions import IsAdmin, default_permissions

from .models import Question
from .serializers import QuestionSerializer


class QuestionFilter(filters.FilterSet):
    """Filter for question."""

    class Meta:
        """Meta info for question filter."""

        model = Question
        fields = ['categories', 'statement']


class QuestionViewSet(ModelViewSet):
    """Question endpoint.

    create:
    Create a new question.

    retrieve:
    Get a specific question information according to its id.

    list:
    Retrieve a paginated list of questionies. Filter statement, choices and
    category.

    update:
    Update a question information.

    partial_update:
    Partially update a question information.

    destroy:
    Delete a question.
    """

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filterset_class = QuestionFilter
    permission_classes = [*default_permissions, IsAdmin]
