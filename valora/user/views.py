from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from user.models import UserProfile
from .serializers import UserProfileSerializer, TempUserProfileSerializer

ID_FAKE = 0


class BasicList(ReadOnlyModelViewSet):

    def get_queryset(self):
        return UserProfile.objects.filter(user__is_superuser=False).order_by('-total_points').distinct()

    def get_category__id(self):
        return ID_FAKE

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        UserProfile.att_sequential(queryset)
        UserProfile.att_pontuacao(self.get_category__id(), category=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RankingAPIView(BasicList):
    queryset = UserProfile.objects.all().order_by('-sequential')
    serializer_class = UserProfileSerializer
    filterset_fields = ['user']
    permission_classes = (permissions.IsAuthenticated,)


class RankingCategoryAPIView(BasicList):
    queryset = UserProfile.objects.all().order_by('-sequential')
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_category__id(self):
        return self.kwargs['category_id']

    def get_queryset(self):
        return UserProfile.objects.filter(user__is_superuser=False,
                                          question_correct__category__id=
                                          self.get_category__id()).order_by('-points').distinct()


class TempRankingAPIView(ReadOnlyModelViewSet):
    queryset = UserProfile.objects.filter().order_by('-points')
    serializer_class = TempUserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


@login_required
def account_redirect(request):
    return redirect('/api_quiz')
