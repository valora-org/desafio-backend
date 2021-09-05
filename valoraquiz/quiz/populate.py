import users.models
import users.choices

from . import models, services


def create_user(email, username, password, type):
    return users.models.User.objects.create(
        email=email, username=username, password=password, type=type
    )


def create_category(title):
    return models.Category.objects.create(title=title)


def create_question(label, category_id):
    return models.Question.objects.create(label=label, category_id=category_id)


def create_answer(label, question_id, is_right):
    return models.Answer.objects.create(
        label=label, question_id=question_id, is_right=is_right
    )


def run():
    player = create_user(
        email="player@email.com",
        username="player",
        password="player123",
        type=users.choices.PLAYER,
    )
    admin = create_user(
        email="admin@email.com",
        username="admin",
        password="admin123",
        type=users.choices.ADMIN,
    )
    fake_category = create_category(title="Machine")

    count = 0
    while count <= 10:
        question = create_question(
            label=f"Question {count}", category_id=fake_category.pk
        )
        for idx in range(3):
            create_answer(
                label=f"Answer {idx}",
                question_id=question.pk,
                is_right=False if idx < 2 else True,
            )
        count += 1

    services.create_quiz(category_id=fake_category.pk, user=player)
    services.create_quiz(category_id=fake_category.pk, user=admin)
