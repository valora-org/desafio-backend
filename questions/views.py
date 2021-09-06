from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from questions.models import Category, Question
from questions.serializers import CategorySerializer, QuestionSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_categories(request):
    user = request.user
    if user.is_staff:
        category = Category.objects.all()
    else:
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
    except IntegrityError:
        message = {"detail": f"Categoria {name} já existe"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_category(request, pk):
    data = request.data
    try:
        category = Category.objects.get(id=pk)
        category.name = data["name"]
        category.save()
        serializer = CategorySerializer(category, many=False)
    except IntegrityError:
        message = {"detail": f"Categoria {data['name']} já existe"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_category(request, pk):
    try:
        category_for_deletion = Category.objects.get(id=pk)
    except ObjectDoesNotExist:
        message = {"detail": f"Categoria ID {pk} não encontrada"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        message = {"detail": f"Valor: {pk} não corresponde a um ID válido"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    # TODO Quando deletear as categorias, implementar para desativar as perguntas
    category_for_deletion.is_active = False
    category_for_deletion.save()
    return Response("Categoria deletada")


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_question(request):
    data = request.data
    user = request.user
    try:
        question = data["question"].title()
        first_answer = data["first_answer"].title()
        second_answer = data["second_answer"].title()
        third_answer = data["third_answer"].title()
        correct_answer = data["correct_answer"]
        if not (
            correct_answer == "1"
            or correct_answer == "2"
            or correct_answer == "3"
        ):
            raise ValueError
        category = Category.objects.get(name=data["category"])
        questions = Question.objects.create(
            question=question,
            category=category,
            registered_by=user,
            first_answer=first_answer,
            second_answer=second_answer,
            third_answer=third_answer,
            correct_answer=data["correct_answer"],
            is_active=True,
        )
        serializer = QuestionSerializer(questions, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        message = {"detail": "Categoria não encontrada"}
    except MultiValueDictKeyError:
        message = {
            "detail": "Verifique se os dados foram informados corretamente"
        }
    except ValueError:
        message = {"detail": "Resposta deve ser entre 1 e 3"}
    except Exception:
        message = {"detail": "Não foi possível cadastrar a pergunta"}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_question(request, pk):
    data = request.data
    user = request.user
    qst_obj = Question.objects.get(id=pk)
    try:
        category = Category.objects.get(name=data["category"])
        qst_obj.question = data["question"].title()
        qst_obj.category = category
        qst_obj.registered_by = user
        qst_obj.first_answer = data["first_answer"].title()
        qst_obj.second_answer = data["second_answer"].title()
        qst_obj.third_answer = data["third_answer"].title()
        correct_answer = data["correct_answer"]
        if not (
            correct_answer == "1"
            or correct_answer == "2"
            or correct_answer == "3"
        ):
            raise ValueError
        qst_obj.correct_answer = correct_answer
        qst_obj.save()
        serializer = QuestionSerializer(qst_obj, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        message = {"detail": "Categoria não encontrada"}
    except MultiValueDictKeyError:
        message = {
            "detail": "Verifique se os dados foram informados corretamente"
        }
    except ValueError:
        message = {"detail": "Resposta deve ser entre 1 e 3"}
    except Exception:
        message = {"detail": "Não foi possível cadastrar a pergunta"}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_question(request, pk):
    try:
        category_for_deletion = Question.objects.get(id=pk)
    except ObjectDoesNotExist:
        message = {"detail": "ID da pergunta não encontrado"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        message = {"detail": "Valor informado não corresponde a um ID válido"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    category_for_deletion.is_active = False
    category_for_deletion.save()
    return Response("Questão deletada")
