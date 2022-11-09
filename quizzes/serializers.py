from categories.serializers import CategorySerializer
from questions.serializers import QuestionSerializer
from questions.models import Question, Alternative
from categories.models import Category
from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    categories = CategorySerializer(many=True)
    questions = QuestionSerializer(many=True)

    def create(self, validated_data):

        title = validated_data.pop("title").title()
        categories = validated_data.pop("categories")
        questions = validated_data.pop("questions")

        quiz = Quiz.objects.create(title=title, **validated_data)

        # Creates and adds all categories in the quiz
        for category in categories:
            category, _ = Category.objects.get_or_create(**category)
            quiz.categories.add(category)

        # Creates and adds all questions in the quiz
        for question in questions:
            alternatives = question.pop("alternatives")

            question, _ = Question.objects.get_or_create(**question)

            # Creates and adds all alternatives for every question in the quiz
            for alternative in alternatives:
                alternative, _ = Alternative.objects.get_or_create(
                    **alternative, question=question
                )

            quiz.questions.add(question)

        return quiz

    def update(self, instance: Quiz, validated_data):

        for key, item in validated_data.items():
            if key == "categories":
                for category in item:
                    category, _ = Category.objects.get_or_create(**category)
                    instance.categories.add(category)

            elif key == "questions":
                for question in item:
                    alternatives = question.pop("alternatives")

                    question, _ = Question.objects.get_or_create(**question)

                    for alternative in alternatives:
                        description = alternative.pop("description")
                        alternative, _ = Alternative.objects.get_or_create(
                            **alternative, description=description, question=question
                        )

                instance.questions.add(question)

            else:
                setattr(instance, key, item)

        instance.save()

        return instance
