from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from quiz.core.permissions import IsPlayer, default_permissions

from . import serializers
from .models import Match


class MatchViewSet(GenericViewSet):
    """Authentication viewset."""

    permission_classes = [*default_permissions, IsPlayer]

    @action(methods=['get'], detail=False, url_path='open', url_name='open')
    def get_open_match(self, request, *args, **kwargs):
        """Get open match of the user."""
        player = request.user
        match = get_object_or_404(Match, player=player)
        print(match.questions_ids)
        serializer = serializers.MatchQuestionsSerializer(
            instance=match.questions, many=True)
        response_data = {'id': match.id, 'questions': serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.NewMatchSerializer)
    @action(methods=['post'], detail=False, url_path='new', url_name='new')
    def new_match(self, request, *args, **kwargs):
        """Create a new match for logged user according to category."""
        context = self.get_serializer_context()
        serializer = serializers.NewMatchSerializer(data=request.data,
                                                    context=context)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,
                        status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=serializers.MatchResponseSerializer)
    @action(methods=['post'],
            detail=False,
            url_path='response',
            url_name='response')
    def answer_match(self, request, *args, **kwargs):
        """Create a new match for logged user according to category."""
        context = self.get_serializer_context()
        serializer = serializers.MatchResponseSerializer(data=request.data,
                                                         context=context)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
