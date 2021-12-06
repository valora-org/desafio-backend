from rest_framework import serializers

from quizzes.models import Answer, Question, Ranking


# Answer Serialiazer used in Answer Views
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


# Answer Serialiazer used in QuizQuestionSerializer to return
# answer text and id only.
class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("text", "id")


# Question Serialiazer used in Question Views
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


# Question Serialiazer used in Get Quiz View. Used to return
# the questions with the 3 possible answers to the player.
class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ("text", "id", "answers")


# Ranking Serialiazer used in Ranking Views.
class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = "__all__"
