from .models import Question, Answer, QuizPage

def question_has_category():
    test_question = new Question("Music","Who sings the song New York New York ?")
    assert test_question.category is not null

def quizpage_has_1_question():
    quizpage = new QuizPage("What's the absolute value of -2345.67 ?",null)
    assert quizpage.question is not null

def question_has_3_answers():
    question = new Question("Music","What's the name of Ozzy's wife?")
    answer1 = new Answer("What's the name of Ozzy's wife?","Sharon",true)
    answer2 = new Answer("What's the name of Ozzy's wife?","Mary",false)
    answer3 = new Answer("What's the name of Ozzy's wife?","Joana",false)

    query_question = Question.objects.get(pk=question.id)
    assert query_question.answer_set.all().length() == 3