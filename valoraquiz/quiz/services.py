from quiz import models


def create_category(title):
    return models.Category.objects.create(title=title)


def get_category_by_id(pk):
    try:
        return models.Category.objects.get(pk=pk)
    except models.Category.DoesNotExist:
        return


def list_categories():
    return models.Category.objects.all()


def update_category(title, pk):
    category = get_category_by_id(pk=pk)
    if not category:
        return

    category.title = title
    category.save()
    return category


def create_quiz(category_id, user):
    questions = models.Question.objects.filter(category_id=category_id).order_by("?")[
        :10
    ]
    if len(questions) < 10:
        raise ValueError("This category has no 10 questions")

    quiz = models.Quiz.objects.create(user=user, category_id=category_id)
    for question in questions:
        quiz.questions.add(question)

    return quiz


def get_quiz_by_id_and_user_id(pk, user_id):
    try:
        return models.Quiz.objects.get(pk=pk, user_id=user_id)
    except models.Quiz.DoesNotExist:
        return


def filter_quiz_by_user_id(user_id):
    return models.Quiz.objects.filter(user_id=user_id)


def update_quiz_answered(quiz, answers, is_finished):
    answers_ids = []
    for answer in answers:
        answers_ids.append(answer["answer_id"])

    quiz.answers.set(answers_ids)

    quiz.is_finished = is_finished

    quiz.save()

    return quiz


def create_question(label, category):
    return models.Question.objects.create(label=label, category=category)


def create_answer(label, question, is_rigth):
    return models.Answer.objects.create(
        label=label, question=question, is_rigth=is_rigth
    )
