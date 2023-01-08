from quizzes.models import Answer
from random import shuffle

class Quizzes:
    def __init__(self, category: str):
        self.category = category
        self.base_quizz = self.get_random_quizz()
        
    def get_random_quizz(self) -> dict:
        """
        Args:
            category (str): Categoria do Quizz

        Returns:
            dict: Quizz aleatório
        """
        
        # Também poderiamos fazer usando .order_by('?') porém fazer isto nos 
        # custaria mais um acesso ao banco de dados, consequentemente isto 
        # tornaria a função mais lenta ao passar do tempo
        anwser_list = list(Answer.objects.filter(category__type_text=self.category))
        return shuffle(anwser_list)[0:10]