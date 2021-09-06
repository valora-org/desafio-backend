from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from questions.models import Category
from questions.serializers import CategorySerializer


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_categories(request):
    category = Category.objects.filter(is_active=True)
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_category(request):
    data = request.data
    try:
        name = data["name"].title()
        category = Category.objects.create(name=name)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    except:
        message = {"detail": "Categoria com esse nome já existe"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    data = request.data
    category.name = data["name"]
    category.save()
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_category(request, pk):
    category_for_deletion = Category.objects.get(id=pk)
    #TODO Quando deletear as categorias, implementar para desativar as perguntas
    category_for_deletion.is_active = False
    category_for_deletion.save()
    return Response("Categoria deletada")
