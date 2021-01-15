from quiz.models import Quiz, SubmitPlayer, Question, Answer, PlayersAnswer
from rest_framework import serializers


class QuizListSerializer(serializers.ModelSerializer):
	"""
		Serializer to return the id, name, category of the model Quiz.

	"""
	class Meta:
		model = Quiz
		fields = ["id", "name", "slug"]
				
class AnswerSerializer(serializers.ModelSerializer):
	"""
		Serializer to return the id, question, label of the model Answer.

	"""
	class Meta:
		model = Answer
		fields = ["id", "question", "label"]


class QuestionSerializer(serializers.ModelSerializer):
	"""
		Serializer to return all fields of the model Question.

	"""

	# Return fields of the answer.
	answer_set = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = "__all__"


class PlayersAnswerSerializer(serializers.ModelSerializer):
	"""
		Serializer to return all fields of the model PlayersAnswer.

	"""
	class Meta:
		model = PlayersAnswer
		fields = "__all__"


class PlayerQuizListSerializer(serializers.ModelSerializer):
	"""
		Serializer to return id, name, category, score of the player.

	"""

	# Retrieval of the score.
	score = serializers.SerializerMethodField()

	class Meta:
		model = Quiz
		fields = ["id", "name", "slug", "score"]

	def get_score(self, obj):
		"""
			Return score of the player.

		"""
		try:
			submit_player = SubmitPlayer.objects.get(user=self.context['request'].user, quiz=obj)
			
			return submit_player.score
		
		except SubmitPlayer.DoesNotExist:
			return None


class SubmitPlayerSerializer(serializers.ModelSerializer):
	"""
		Serializer to return all fields of the model SubmitPlayer.

	"""
	# Return fields of the answer player.
	playersanswer_set = PlayersAnswerSerializer(many=True)

	class Meta:
		model = SubmitPlayer
		fields = "__all__"


class QuizResultSerializer(serializers.ModelSerializer):
	"""
		Serializer to return the results obtained to the player.

	"""

	# Retrieval of the player.
	submit_player_set = serializers.SerializerMethodField()
	# Return fields of the question.
	question_set = QuestionSerializer(many=True)

	class Meta:
		model = Quiz
		fields = "__all__"

	def get_submit_player_set(self, obj):
		"""
			Return player submissions.

		"""
		try:
			submit_player = SubmitPlayer.objects.get(user=self.context['request'].user, quiz=obj)
			serializer = SubmitPlayerSerializer(submit_player)
			return serializer.data

		except SubmitPlayer.DoesNotExist:
			return None 

		
