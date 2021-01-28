import pytest
from quiz import models as qz
from accounts.models import User

@pytest.mark.django_db
def test_quiz_create():
    
Function to test creation of the Quiz model
	

    
    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        slug="quiz-test",
    )

    # Asserts of test
    assert quiz.name == "Quiz Test"
    assert quiz.slug == "quiz-test"

@pytest.mark.django_db
def test_question_create():
    
		#Function to test creation of the Question model
	

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
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
    
		#Function to test creation of the Answer model
	
  
    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
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
    
		#Function to test creation of the SubmitPlayer model
	

    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
        slug="quiz-test",
    )

    # Create object user
    user = User.objects.create(
        username="user"
    )

    # Create object submit player
    quiztaker = qz.QuizTaker.objects.create(
        quiz=quiz,
        user=user
    )

    # Asserts of test
    assert quiztaker.quiz == quiz
    assert quiztaker.user == user
    assert quiztaker.score == 0

@pytest.mark.django_db
def test_players_answer_create():
    
		#Function to test creation of the PlayersAnswer model
	
    # Create object quiz
    quiz = qz.Quiz.objects.create(
        name="Quiz Test",
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
    user = User.objects.create(
        username="user"
    )

    # Create object submit player
    quiztaker = qz.QuizTaker.objects.create(
        quiz=quiz,
        user=user
    )

    # Create object players answer
    users_answer = qz.usersAnswer.objects.create(
        quiztaker = quiztaker,
        question=question,
        answer=answer
    )

    # Asserts of test
    assert users_answer.quiztaker == quiztaker
    assert users_answer.question == question
    assert users_answer.answer == answer