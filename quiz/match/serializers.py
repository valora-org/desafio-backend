from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from quiz.questions.models import Category
from quiz.questions.models import Question

from .models import Match, MatchResponse

# New match


class MatchQuestionsSerializer(serializers.ModelSerializer):
    """Format a question for output on creating a new match."""

    class Meta:
        """Meta information for login serializer."""

        model = Question
        fields = ['id', 'statement', 'choices']


class NewMatchSerializer(serializers.Serializer):
    """Serializer for new match request."""

    player = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.PrimaryKeyRelatedField(
        many=False,
        required=True,
        queryset=Category.objects.all(),
        write_only=True)

    def create_match(self, player, category):
        """Create a new unique match for user according to category."""
        try:
            match = Match.objects.create(player=player, category=category)
            match.save()
            return match
        except IntegrityError:
            msg = 'User has an open quiz, finish before create a new one'
            raise serializers.ValidationError({'player': _(msg)})

    def validate(self, attrs):
        """Validate credentials and get user tokens."""
        match = self.create_match(**attrs)
        questions = match.get_shuffle_questions()
        questions_data = MatchQuestionsSerializer(questions, many=True)
        return {'id': match.id, 'questions': questions_data.data}


# Response


class MatchResponseInputSerializer(serializers.Serializer):
    """Validate input response data."""

    question = serializers.PrimaryKeyRelatedField(
        many=False,
        required=True,
        queryset=Question.objects.all(),
        write_only=True)
    choice_index = serializers.IntegerField()


class MatchResponseSerializer(serializers.Serializer):
    """Handle response data."""

    player = serializers.HiddenField(default=serializers.CurrentUserDefault())
    responses = MatchResponseInputSerializer(many=True)

    def check_duplicated_responses(self, responses):
        """Check for duplicated responses."""
        responses_set = {response.question.id for response in responses}
        if len(responses_set) != len(responses):
            msg = 'Check for duplicated answers'
            raise serializers.ValidationError({'responses': _(msg)})

    def validate(self, attrs):
        """Check responses and delete match instance."""
        player = attrs.get('player')
        responses = [MatchResponse(**r) for r in attrs['responses']]
        self.check_duplicated_responses(responses)
        match = get_object_or_404(Match, player=player)
        points, score = match.check_responses(responses)
        match.delete()
        return {'points': points, 'score': score}
