from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Category, Question, Answer, Classification


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True)

    class Meta:
        model = Question
        fields = ('id', 'category', 'question_text', 'choice_A', 'choice_B', 'choice_C',)


class AnswerSerializers(serializers.ModelSerializer):
    # category = CategorySerializer(required=True)
    # question = QuestionSerializer(required=True)
    author = get_user_model()

    def validate(self, attrs):

        if not attrs['author_answer'] in ['A', 'B', 'C']:
            raise serializers.ValidationError("Invalid answer")

        return attrs

    def create(self, validated_data):

        """
        Checks if the answer has already been given
        """
        new_answer = Answer.objects.filter(question=validated_data['question'],
                                          author=validated_data['author'],
                                          category=validated_data['category'])
        # Create a new answer
        if len(new_answer) == 0:
            Answer.objects.create(**validated_data)

        # Take the question related to the answer
        question = Question.objects.filter(pk=validated_data['question'])

        # Check if is the right answer
        new_answer.is_correct = True if question.right_choice == new_answer.author_answer else False
        new_answer.save()

        # Update the classification for that user
        classification = Classification.objects.filter(author=new_answer.author, category=new_answer.category)
        if len(classification) == 0:
            new_classification = Classification()
            new_classification.author = new_answer.author
            new_classification.category = new_answer.category
            new_classification.points = 1 if new_answer.is_correct else 0
            new_classification.save()

        # Update points for the user
        else:
            if new_answer.is_correct:
                classification[0].points += 1
            else:
                classification[0].points -= 1
                if classification[0].points < 0:
                    classification[0].points = 0
            classification.save()

        return new_answer

    class Meta:
        model = Answer
        fields = ('category', 'question', 'author', 'author_answer',)


class ClassificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'
