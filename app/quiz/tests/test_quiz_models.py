import pytest
from quiz import models as qz
from accounts import models as ac

@pytest.mark.django_db
def test_category_create():
    """
		Function to test creation of the Category model

	"""
    # Create object category
    category = qz.Category.objects.create(
        title = "test"
    )

    # Asserts of test
    assert category.title == "test"


@pytest.mark.django_db
def test_quiz_create():
    """
		Function to test creation of the Quiz model

	"""

    # Create object category
    category = qz.Category.objects.create(
        title = "test"
    )

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        category = category,
        slug="quiz-test",
    )

    # Asserts of test
    assert quiz.name == "Quiz Test"
    assert quiz.category == category
    assert quiz.slug == "quiz-test"

@pytest.mark.django_db
def test_question_create():
    """
		Function to test creation of the Question model

	"""
    # Create object category
    category = qz.Category.objects.create(
        title = "test"
    )

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        category= category,
        slug="quiz-test",
    )

    # Create object question
    question = qz.Question.objects.create(
        label="Question label",
        quiz=quiz
    )
    
    # Asserts of test
    assert question.quiz == quiz
    assert question.label == "Question label"

@pytest.mark.django_db
def test_answer_create():
    """
		Function to test creation of the Answer model

	"""
    # Create object category
    category = qz.Category.objects.create(
        title = "test"
    )

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        category= category,
        slug="quiz-test",
    )

    # Create object question
    question = qz.Question.objects.create(
        label="Question label",
        quiz=quiz
    )

    # Create object answer
    answer = qz.Answer.objects.create(
        label="Answer label",
        question=question
    )
    
    # Asserts of test
    assert answer.question == question
    assert answer.label == "Answer label"
    assert answer.is_correct == False

@pytest.mark.django_db
def test_submit_player_create():
    """
		Function to test creation of the SubmitPlayer model

	"""

    # Create object category
    category = qz.Category.objects.create(
        title = "test"
    )

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        category= category,
        slug="quiz-test",
    )

    # Create object user
    user = ac.User.objects.create(
        username="user"
    )

    # Create object submit player
    submit_player = qz.SubmitPlayer.objects.create(
        quiz=quiz,
        user=user
    )
    
    # Asserts of test
    assert submit_player.quiz == quiz
    assert submit_player.user == user
    assert submit_player.score == 0

@pytest.mark.django_db
def test_players_answer_create():
    """
		Function to test creation of the PlayersAnswer model

	"""

    # Create object category
    category = qz.Category.objects.create(
        title = "test"
    )

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        category= category,
        slug="quiz-test",
    )

    # Create object question
    question = qz.Question.objects.create(
        label="Question label",
        quiz=quiz
    )
    
    # Create object answer
    answer = qz.Answer.objects.create(
        label="Answer label",
        question=question
    )

    # Create object user
    user = ac.User.objects.create(
        username="user"
    )

    # Create object submit player
    submit_player = qz.SubmitPlayer.objects.create(
        quiz=quiz,
        user=user
    )

    # Create object players answer
    players_answer = qz.PlayersAnswer.objects.create(
        submit_player = submit_player,
        question=question,
        answer=answer
    )
    
    # Asserts of test
    assert players_answer.submit_player == submit_player
    assert players_answer.question == question
    assert players_answer.answer == answer