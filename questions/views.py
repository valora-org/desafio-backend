import random

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from rank.models import Rank
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from questions.models import Category, Question
from questions.serializers import (
    CategorySerializer,
    QuestionSerializer,
    QuizCategorySerializer,
    QuizSerializer,
)


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
        category_for_del = Category.objects.get(id=pk)
    except ObjectDoesNotExist:
        message = {"detail": f"Categoria ID {pk} não encontrada"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        message = {"detail": f"Valor: {pk} não corresponde a um ID válido"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    category_for_del.is_active = False
    category_for_del.save()
    questions_for_del = Question.objects.filter(category=category_for_del)
    for question in questions_for_del:
        question.is_active = False

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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_quiz(request):
    category = Category.objects.filter(is_active=True)
    serializer = QuizCategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def quiz_questions(request, pk):
    try:
        category = Category.objects.get(id=pk)
        lst_questions = Question.objects.filter(category=category).values_list(
            "id", flat=True
        )
        rdm_questions = random.sample(list(lst_questions), 10)
        questions = Question.objects.filter(id__in=rdm_questions)
        serializer = QuizSerializer(questions, many=True)
        return Response(serializer.data)
    except ValueError:
        message = {"detail": f"Não existe categoria com o ID {pk}"}
    except ObjectDoesNotExist:
        message = {"detail": f"Não existe categoria com o ID {pk}"}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def answers_question(request):
    user = request.user
    data = request.data
    response = {}
    score = 0
    category = None
    for k, v in data.items():
        try:
            question = Question.objects.get(id=k)
        except ObjectDoesNotExist:
            message = {"detail": f"Não existe pergunta com o ID {k}"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        if category:
            if category != question.category:
                message = {
                    "detail": f"Questão ID {k},  pertence a outra categoria"
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            category = question.category
        if question.correct_answer == v:
            score += 1
        else:
            if score > 0:
                score -= 1
    response["Jogada Atual"] = f"Você obteve {score} Pts"
    Rank.objects.create(score=score, category=category, profile=user)
    rank = Rank.objects.filter(profile=user)
    rank_global = rank.values_list("score", flat=True)
    rank_by_category = rank.filter(category=category).values_list(
        "score", flat=True
    )
    score_global = sum(rank_global)
    score_by_category = sum(rank_by_category)
    response["Pontuação global"] = f"Sua pontuação total: {score_global} Pts"
    response[
        "Pontuação global na categoria"
    ] = f"Sua pontuação total nessa categoria: {score_by_category} Pts"

    return Response(response)
