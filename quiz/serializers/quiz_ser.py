from rest_framework import serializers 
from quiz.models.quiz import *
import functools 
from .question_ser import QuestionPointSerializer
from quiz.models.rank import *

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz 
        fields = "__all__"


class QuizField(serializers.RelatedField):
    def to_representation(self, data):
        return data.id

    def to_internal_value(self, data):
        try:
            item  = Quiz.objects.get(id=data)
        except Quiz.DoesNotExist:
            raise serializers.ValidationError({'Quiz':'Passe um item válido'})
        return item

class QuizQuestionAnswerSerializer(serializers.Serializer):
    questions = QuestionPointSerializer(many=True)
    
    class Meta:
        fields = ['questions']
        extra_kwargs = {
            'questions': {'write_only':True}
        }
    
    def get_point_value(self,question_id,answer):
        correct_option = question_id.options.get(is_correct=True)
        condition  = answer == correct_option
        point = 1 if condition else -1 

        return point
    
    def create_or_update_player_rank(self,player,quiz,value):
        player_rank,created = PlayerRank.objects.get_or_create(player=player)
        points = player_rank.points.all()
        quiz_point = points.filter(quiz=quiz)

        if quiz_point.exists():
            point = quiz_point.last()
            point.__setattr__('value',value)
            point.save()
        else:
            point = Point.objects.create(
                quiz=quiz,
                value=value
            )
        player_rank.points.add(point)

        player_rank.set_total_points()
        print(PlayerRank.objects.order_by("-total_points").filter(total_points__lte=player_rank.total_points))
        total_rank = PlayerRank.objects.order_by("-total_points").filter(total_points__lte=player_rank.total_points).count()

        return {
            'total_points':player_rank.total_points,
            'quiz_points':value,
            'rank': total_rank + 1
        }
    

    def create(self,validated):
        quiz = self.context['quiz']
        player = self.context['request'].user 

        questions = validated['questions']      
        mapped = list(map(lambda x: self.get_point_value(x['id'],x['answer']),questions))
        reduced = functools.reduce(lambda a,b: a +b,mapped)
        reduced = reduced if reduced >= 0 else 0
        response = self.create_or_update_player_rank(player,quiz,reduced)

        return response