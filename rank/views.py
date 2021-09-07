from questions.models import Category
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rank.models import Rank
from rank.serializers import RankSerializer


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_rank(request):
    ranking = Rank.objects.all()
    serializer = RankSerializer(ranking, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_rank_by_user(request):
    response = {}
    user = request.user
    lst_score = Rank.objects.filter(profile=user).values_list(
        "score", flat=True
    )
    score = sum(lst_score)
    response["Pontuação global"] = score
    return Response(response)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_rank_by_category(request, pk):
    response = {}
    user = request.user
    try:
        category = Category.objects.get(id=pk)
    except ObjectDoesNotExist:
        message = {"detail": "Categoria não encontrada"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    lst_score = Rank.objects.filter(
        profile=user, category=category
    ).values_list("score", flat=True)
    score = sum(lst_score)
    response["Categoria"] = category.name
    response["Pontuação global"] = score
    return Response(response)
