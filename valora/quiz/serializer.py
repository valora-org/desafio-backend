from rest_framework import serializers

from quiz import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    start_quiz_url = serializers.SerializerMethodField('get_start_quiz')
    ranking_category = serializers.SerializerMethodField('get_ranking_category')

    # Usando HyperlinkedModelSerializer para ajudar na movientação das pags

    def get_start_quiz(self, obj):
        return "http://127.0.0.1:8000/quiz/%d" % obj.id

    def get_ranking_category(self, obj):
        return "http://127.0.0.1:8000/user/ranking_category/%d" % obj.id

    class Meta:
        model = models.Category
        fields = ('id', 'url', 'category', 'start_quiz_url', 'ranking_category')


class QuestionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id', 'url', 'category', 'question', 'option_a', 'option_b', 'option_c', 'correct')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id', 'question', 'option_a', 'option_b', 'option_c', 'correct_user')
