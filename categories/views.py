from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer
from users.utils import Is_admin_or_read
from django.db import IntegrityError
from .models import Category
from django.http import Http404


class CategoryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Is_admin_or_read]

    def get(self, _):

        categories = Category.objects.all()
        categories_serialized = CategorySerializer(categories, many=True)

        return Response(
            {"categories": categories_serialized.data}, status=status.HTTP_200_OK
        )

    def post(self, request: Request):

        try:
            category_serialized = CategorySerializer(data=request.data)
            category_serialized.is_valid(raise_exception=True)
            category_serialized.save()

            return Response(category_serialized.data, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response(
                {"message": "A category with the provided name already exists"},
                status=status.HTTP_409_CONFLICT,
            )


class CategorySoloView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Is_admin_or_read]

    def get(self, _, category_id: int):

        try:
            category = get_object_or_404(Category, id=category_id)
            category_serialized = CategorySerializer(category)

            return Response(
                {"category": category_serialized.data}, status=status.HTTP_200_OK
            )

        except Http404:
            return Response(
                {"message": "category not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request: Request, category_id: int):

        try:
            category = get_object_or_404(Category, id=category_id)
            category_serialized = CategorySerializer(
                category, request.data, partial=True
            )
            category_serialized.is_valid(raise_exception=True)
            category_serialized.save()

            return Response(
                {"category": category_serialized.data}, status=status.HTTP_200_OK
            )

        except Http404:
            return Response(
                {"message": "category not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except IntegrityError:
            return Response(
                {"message": "'name' field must be unique"},
                status=status.HTTP_409_CONFLICT,
            )

        except KeyError as error:
            return Response(
                {"Missing fields": error.args}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, _, category_id: int):

        try:
            category = get_object_or_404(Category, id=category_id)
            category.delete()

            return Response("", status=status.HTTP_204_NO_CONTENT)

        except Http404:
            return Response(
                {"message": "category not found"}, status=status.HTTP_404_NOT_FOUND
            )
