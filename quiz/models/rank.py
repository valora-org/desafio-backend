from django.db import models 
from .quiz import Quiz 
from user_auth.models.profiles import Player
import functools

class Point(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    value = models.IntegerField(default=0)


class PlayerRank(models.Model):
    player = models.OneToOneField(Player,on_delete=models.CASCADE) 
    points = models.ManyToManyField(Point)
    total_points = models.IntegerField(default=0)
    def create_or_update_point(self,total_point):
        self.value = total_point
        self.save()
    
    
    # override points according quiz ralized
    def set_total_points(self):
        points = list(self.points.all().values('value'))
        reduced = (functools.reduce(lambda a,b: int(a)+int(b),points))
        self.total_points = reduced['value']
        self.save()
