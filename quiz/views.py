from rest_framework import viewsets, mixins
from .models import Question
from .serializers import QuestionSerializer, QuestionListSerializer
from .permissions import UserPermissions
from .mixins import ActionBasedSerializerMixin


class QuestionViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                      mixins.ListModelMixin, ActionBasedSerializerMixin,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    permission_classes = [UserPermissions]
    serializer_classes = {
        'list': QuestionListSerializer,
        'default': QuestionSerializer
    }
