from quizzes.models import Question
from random import shuffle
from rest_framework.serializers import ValidationError
from accounts.models import User

class Quizzes:
    def __init__(self, category: str = None, quiz: dict = None):
        self.category = category
        self.base_quiz = self.get_random_quiz() if not quiz else quiz
        
    def get_random_quiz(self) -> dict:
        """
        Args:
            category (str): Categoria do quiz

        Returns:
            dict: quiz aleatório
        """
        
        # Também poderiamos fazer usando .order_by('?') porém fazer isto nos 
        # custaria mais um acesso ao banco de dados, consequentemente isto 
        # tornaria a função mais lenta ao passar do tempo
        question_list = list(Question.objects.filter(category__type_text=self.category).values_list('id', flat=True))
        if len(question_list) < 10:
            raise(ValidationError("Não foi possível criar um quiz, número de perguntas insuficiente. Consulte um administrador!"))
        # Randomiza perguntas
        shuffle(question_list)
        return {
            "category":self.category,
            "questions":question_list[0:10]
        }

    def get_first_quiz_question(self) -> Question:
        """
        Devolve uma pergunta aleatória do quiz atual
        Returns:
            Question: Pergunta aleatória
        """
        return Question.objects.filter(id=self.base_quiz['questions'][0]).first()
    
    def randomize_quiz_questions(self) -> dict:
        """
        Randomiza o quiz atual
        Returns:
            dict: Quiz randomizado
        """
        shuffle(self.base_quiz['questions'])
        return self.base_quiz

