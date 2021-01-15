from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from quiz.models import Answer, Question, Quiz, SubmitPlayer, PlayersAnswer
from accounts.models import User
from quiz.serializers import PlayerQuizListSerializer, QuizListSerializer, QuizResultSerializer

class PlayerQuizList(generics.ListAPIView):
	"""
		View for the player to view their quizzes and scores.

	"""

	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Respective serializer
	serializer_class = PlayerQuizListSerializer

	def get_queryset(self, *args, **kwargs):
		"""
			GET method

		"""

		# Get all objects
		queryset = Quiz.objects.filter(submitplayer__user=self.request.user)
		query = self.request.GET.get("q")

		# Condition to differentiate by name
		if query:
			queryset = queryset.filter(
				Q(name__icontains=query)
			).distinct()

		# Return response
		return queryset


class QuizList(generics.ListAPIView):
	"""
		View for the player to view all quizzes.

	"""

	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Respective serializer
	serializer_class = QuizListSerializer
	
	def get_queryset(self, *args, **kwargs):
		"""
			GET method

		"""

		# Get all objects
		queryset = Quiz.objects.all()
		query = self.request.GET.get("q")

		# Condition to differentiate by name
		if query:
			queryset = queryset.filter(
				Q(name__icontains=query)
			).distinct()

		# Return response
		return queryset


class SubmitQuiz(generics.GenericAPIView):
	"""
		View for the player submit answer for respective question.

	"""

	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Respective serializer
	serializer_class = QuizResultSerializer

	def post(self, request, *args, **kwargs):
		"""
			POST method

		"""

		# Get respective quiz
		quiz = Quiz.objects.get(slug=self.kwargs['slug'])

		# User requests
		question_id = request.data['question']
		answer_id = request.data['answer']
		
		# Create or Get object
		submit_player, created = SubmitPlayer.objects.get_or_create(user=self.request.user, quiz=quiz)
		question = get_object_or_404(Question, id=question_id)
		
		# Save answer
		if answer_id is not None:
			answer = get_object_or_404(Answer, id=answer_id)
			obj, created = PlayersAnswer.objects.get_or_create(submit_player=submit_player, question=question)
			obj.answer = answer
			obj.save()

		# Add and save the score
		correct_answers = 0

		for players_answer in PlayersAnswer.objects.filter(submit_player=submit_player):
			answer = Answer.objects.get(question=players_answer.question, is_correct=True)
			
			if players_answer.answer == answer:
				correct_answers += 1

		submit_player.score = correct_answers
		
		submit_player.save()

		# Return response
		return Response(self.get_serializer(quiz).data)


class GetQuiz(generics.GenericAPIView):
	"""
		View for the player to see the questions and answers to the quiz.

	"""

	# Authentication required
	permission_classes = [
		permissions.IsAuthenticated
	]

	# Respective serializer
	serializer_class = QuizResultSerializer
	

	def get(self, request, *args, **kwargs):
		"""
			GET method

		"""

		# Get object
		quiz = Quiz.objects.get(slug=self.kwargs['slug'])

		# Return response
		return Response(self.get_serializer(quiz).data)
