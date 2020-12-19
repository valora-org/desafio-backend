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

    author = get_user_model()

    def validate(self, attrs):

        if not attrs['author_answer'] in ['A', 'B', 'C']:
            raise serializers.ValidationError("Invalid answer")

        return attrs

    def create(self, validated_data):

        # Checks if the answer has already been given
        if not Answer.objects.filter(question=validated_data['question'],
                                     author=validated_data['author'],
                                     category=validated_data['category']).exists():

            Answer.objects.create(**validated_data)

        new_answer = Answer.objects.filter(question=validated_data['question'],
                                           author=validated_data['author'],
                                           category=validated_data['category']).first()

        new_answer = self.update(new_answer, validated_data)

        # Take the question related to the answer
        question = Question.objects.filter(pk=new_answer.question.id).first()

        # Check if is the right answer
        new_answer.is_correct = True if question.right_choice == new_answer.author_answer else False
        new_answer.save()

        # Update the classification for that user
        if not Classification.objects.filter(author=new_answer.author, category=new_answer.category).exists():
            nc = Classification()
            nc.author = new_answer.author
            nc.category = new_answer.category
            nc.points = 1 if new_answer.is_correct else 0
            nc.save()

        # Update points for the user
        else:
            c = Classification.objects.filter(author=new_answer.author, category=new_answer.category).first()
            if new_answer.is_correct:
                c.points += 1
            else:
                c.points = 0 if c.points-1 < 0 else c.points-1
            c.save()

        return new_answer

    def update(self, instance, validated_data):
        answer = Answer.objects.filter(pk=instance.pk).first()
        answer.author_answer = validated_data['author_answer']
        answer.save()
        return answer

    class Meta:
        model = Answer
        fields = ('category', 'question', 'author', 'author_answer', 'is_correct')


class ClassificationSerializers(serializers.ModelSerializer):

    author = get_user_model()
    category = CategorySerializer(required=True)

    class Meta:
        model = Classification
        fields = ('author', 'points', 'category',)
