from django.forms.widgets import TextInput
from rest_framework import serializers 
from quiz.models.question import *

class OptionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option 
        fields = ["id",'text']

class QuestionGetSimpleSerializer(serializers.ModelSerializer):
    options = OptionSimpleSerializer(many=True)
    class Meta:
        model = Question 
        fields = ["id","enunciation","options"]


class OptionField(serializers.RelatedField):
    def to_representation(self, data):
        return data.id

    def to_internal_value(self, data):
        try:
            item  = Option.objects.get(id=data)
        except Option.DoesNotExist:
            raise serializers.ValidationError({'option':'Passe uma opção válida'})
        return item


class QuestionField(serializers.RelatedField):
    def to_representation(self, data):
        return data.id

    def to_internal_value(self, data):
        try:
            item  = Question.objects.get(id=data)
        except Question.DoesNotExist:
            raise serializers.ValidationError({'Question':'Passe uma questão válida'})
        return item

class QuestionPointSerializer(serializers.Serializer):
    id = QuestionField(queryset=Question.objects.all())
    answer = OptionField(queryset=Option.objects.all())
    point_value = serializers.SerializerMethodField()
    
    class Meta:
        fields = ['id','answer','point_value']
    
    def get_point_value(self):
        correct_option = self.id.options.get(is_correct=True)
        condition  = self.answer == correct_option
        point = 1 if condition else -1 

        return point