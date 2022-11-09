from .models import Question, Alternative
from rest_framework import serializers


class AlternativeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    answer = serializers.IntegerField()
    alternatives = AlternativeSerializer(many=True)

    def create(self, validated_data):

        alternatives = validated_data.pop("alternatives")

        question = Question.objects.create(**validated_data)

        # Creates all the alternatives and add them to the question
        for alternative in alternatives:
            alternative, _ = Alternative.objects.get_or_create(
                **alternative, question=question
            )
            question.alternatives.add(alternative)

        return question

    def update(self, instance: Question, validated_data):

        for key, item in validated_data.items():

            # check if there's alternatives and update them
            if key == "alternatives":
                for alternative in item:
                    alternative, _ = Alternative.objects.get_or_create(
                        **alternative, question=instance
                    )

            else:
                setattr(instance, key, item)

        instance.save()

        return instance
