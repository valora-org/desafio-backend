from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ranking(models.Model):
    player = models.ForeignKey(
        User,
        related_name="ranking",
        verbose_name="Player",
        on_delete=models.CASCADE,
    )
    category = models.CharField(verbose_name="Categoria", max_length=100)
    points = models.IntegerField(verbose_name="Pontos", default=0)

    def increase_point(self):
        self.points += 1
        self.save()
    
    def decrease_point(self):
        if not self.points == 0:
            self.points -= 1
            self.save()
            
    def position_in_ranking(self):
        for position, ranking in enumerate(Ranking.objects.filter(category=self.category).order_by('-points')):
            if ranking == self:
                return position + 1
        