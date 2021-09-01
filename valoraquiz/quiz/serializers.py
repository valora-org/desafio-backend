from rest_framework import serializers

from quiz import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        read_only_fields = ("id",)
        fields = [
            "id",
            "title",
        ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        read_only_fields = ("id",)
        fields = [
            "id",
            "label",
            "category",
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        read_only_fields = ("id",)
        fields = [
            "id",
            "label",
            "question",
            "is_right",
        ]


class QuizQuestionAnswerAvailableDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
    is_right = serializers.BooleanField()


class QuizQuestionDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
    category_id = serializers.IntegerField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation[
            "answers_available"
        ] = QuizQuestionAnswerAvailableDetailSerializer(
            instance.answer_set.all(), many=True
        ).data
        return representation


class QuizAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()


class QuizCreateSerializer(serializers.Serializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all()
    )


class QuizDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    is_finished = serializers.BooleanField()
    questions = QuizQuestionDetailSerializer(many=True)
    answers = AnswerSerializer(many=True)


class QuizAnsweredSerializer(serializers.Serializer):
    answers = QuizAnswerSerializer(many=True)
    is_finished = serializers.BooleanField()
